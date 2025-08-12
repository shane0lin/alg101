from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Optional, Dict, Tuple
import time
import threading
import itertools

# -----------------------------
# Enums & Constants
# -----------------------------

class VehicleSize(Enum):
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()

class PaymentStatus(Enum):
    UNPAID = auto()
    PAID = auto()
    VOID = auto()

# Contiguous spots a bus requires
BUS_SPOTS_NEEDED = 5

# -----------------------------
# Vehicles
# -----------------------------

class Vehicle:
    """Abstract vehicle.

    Attributes
    ----------
    license_plate : str
        Unique identifier for the vehicle.
    size : VehicleSize
        Size category of the vehicle.
    spots_needed : int
        Number of spots this vehicle needs (1 for most, 5 for bus).
    electric : bool
        Whether the vehicle is electric (may prefer/require charging spots).
    """

    def __init__(self, license_plate: str, size: VehicleSize, spots_needed: int = 1, electric: bool = False):
        self.license_plate = license_plate
        self.size = size
        self.spots_needed = spots_needed
        self.electric = electric

    def can_fit_in_spot(self, spot: "ParkingSpot") -> bool:
        """Override in subclasses if special logic needed.
        Default rule: vehicle fits if vehicle.size <= spot.size.
        Electric vehicles can also take non-electric spots (policy-dependent).
        """
        size_order = {VehicleSize.SMALL: 0, VehicleSize.MEDIUM: 1, VehicleSize.LARGE: 2}
        return size_order[self.size] <= size_order[spot.size]

    def __repr__(self):
        return f"{self.__class__.__name__}({self.license_plate})"

class Motorcycle(Vehicle):
    def __init__(self, license_plate: str, electric: bool = False):
        super().__init__(license_plate, VehicleSize.SMALL, spots_needed=1, electric=electric)

class Car(Vehicle):
    def __init__(self, license_plate: str, electric: bool = False):
        super().__init__(license_plate, VehicleSize.MEDIUM, spots_needed=1, electric=electric)

class Bus(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleSize.LARGE, spots_needed=BUS_SPOTS_NEEDED, electric=False)

    def can_fit_in_spot(self, spot: "ParkingSpot") -> bool:
        # Buses only fit in LARGE spots
        return spot.size == VehicleSize.LARGE

# -----------------------------
# Core Domain Models
# -----------------------------

@dataclass
class ParkingSpot:
    level_index: int
    row: int
    number: int
    size: VehicleSize
    electric: bool = False
    occupied_by: Optional[Vehicle] = None

    def is_free(self) -> bool:
        return self.occupied_by is None

    def can_fit(self, vehicle: Vehicle) -> bool:
        if not self.is_free():
            return False
        return vehicle.can_fit_in_spot(self)

    def park(self, vehicle: Vehicle) -> None:
        if not self.can_fit(vehicle):
            raise ValueError("Vehicle cannot fit in this spot or spot is occupied.")
        self.occupied_by = vehicle

    def leave(self) -> None:
        self.occupied_by = None

    @property
    def id(self) -> Tuple[int, int, int]:
        return (self.level_index, self.row, self.number)

    def __repr__(self):
        flags = []
        if self.electric:
            flags.append("E")
        if not self.is_free():
            flags.append(f"occ={self.occupied_by.license_plate}")
        flag_str = f" ({','.join(flags)})" if flags else ""
        return f"Spot L{self.level_index}-R{self.row}-N{self.number}:{self.size.name}{flag_str}"

@dataclass
class ParkingTicket:
    ticket_id: int
    license_plate: str
    spot_ids: List[Tuple[int, int, int]]  # list of (level,row,number) for multi-spot vehicles
    entry_ts: float
    exit_ts: Optional[float] = None
    amount_cents: Optional[int] = None
    status: PaymentStatus = PaymentStatus.UNPAID

# -----------------------------
# Pricing / Rate Strategy
# -----------------------------

class RateCalculator:
    """Strategy for computing parking fees.

    Example policy:
      - First 30 minutes: free grace period
      - Then $3 per hour for SMALL, $4 for MEDIUM, $5 for LARGE (pro-rated by minute)
      - Electric spots add +$1/hour premium if actually parked in electric spot
    """

    BASE_RATE_CENTS = {
        VehicleSize.SMALL: 300,
        VehicleSize.MEDIUM: 400,
        VehicleSize.LARGE: 500,
    }
    ELECTRIC_PREMIUM_PER_HOUR_CENTS = 100
    GRACE_PERIOD_SECONDS = 30 * 60

    def calculate(self, vehicle: Vehicle, seconds: int, used_electric_spot: bool) -> int:
        if seconds <= self.GRACE_PERIOD_SECONDS:
            return 0
        hours = seconds / 3600.0
        base = self.BASE_RATE_CENTS[vehicle.size] * hours
        if used_electric_spot:
            base += self.ELECTRIC_PREMIUM_PER_HOUR_CENTS * hours
        return int(round(base))

# -----------------------------
# Level & Lot
# -----------------------------

class Level:
    """Represents a single level (floor) in the garage.

    We model spots as rows for simple adjacency checks. Buses require
    contiguous LARGE spots within the same row.
    """

    def __init__(self, index: int, rows: List[List[ParkingSpot]]):
        self.index = index
        self.rows = rows
        self._lock = threading.RLock()
        # Precompute counts for quick availability
        self._recount()

    def _recount(self):
        self.free_counts = {VehicleSize.SMALL: 0, VehicleSize.MEDIUM: 0, VehicleSize.LARGE: 0}
        self.free_electric = 0
        for row in self.rows:
            for s in row:
                if s.is_free():
                    self.free_counts[s.size] += 1
                    if s.electric:
                        self.free_electric += 1

    def available_summary(self) -> Dict[str, int]:
        with self._lock:
            self._recount()
            return {
                "SMALL": self.free_counts[VehicleSize.SMALL],
                "MEDIUM": self.free_counts[VehicleSize.MEDIUM],
                "LARGE": self.free_counts[VehicleSize.LARGE],
                "ELECTRIC": self.free_electric,
            }

    def _iter_spots(self):
        for r, row in enumerate(self.rows):
            for c, spot in enumerate(row):
                yield r, c, spot

    def find_spots_for_vehicle(self, vehicle: Vehicle) -> Optional[List[ParkingSpot]]:
        """Find suitable spots for vehicle, nearest-first by simple scan order.

        - For bus: return 5 contiguous LARGE free spots in same row.
        - For electric cars: prefer electric spots if available; fall back to regular.
        - For motorcycles/cars: first fit based on size rules.
        """
        with self._lock:
            if isinstance(vehicle, Bus):
                return self._find_contiguous_large(vehicle.spots_needed)
            # Prefer electric if EV needs 1 spot and such spot fits
            if vehicle.electric and vehicle.spots_needed == 1:
                for _, _, spot in self._iter_spots():
                    if spot.electric and spot.can_fit(vehicle):
                        return [spot]
            # General first-fit
            for _, _, spot in self._iter_spots():
                if spot.can_fit(vehicle):
                    return [spot]
            return None

    def _find_contiguous_large(self, count: int) -> Optional[List[ParkingSpot]]:
        for r, row in enumerate(self.rows):
            run: List[ParkingSpot] = []
            for spot in row:
                if spot.size == VehicleSize.LARGE and spot.is_free():
                    if run and run[-1].row != r:
                        run = []  # safety, should not trigger
                    run.append(spot)
                    if len(run) == count:
                        return run
                else:
                    run = []
        return None

    def park(self, vehicle: Vehicle) -> Optional[List[ParkingSpot]]:
        with self._lock:
            spots = self.find_spots_for_vehicle(vehicle)
            if not spots:
                return None
            for s in spots:
                s.park(vehicle)
            return spots

    def unpark(self, vehicle: Vehicle) -> List[ParkingSpot]:
        with self._lock:
            freed: List[ParkingSpot] = []
            for _, _, spot in self._iter_spots():
                if spot.occupied_by and spot.occupied_by.license_plate == vehicle.license_plate:
                    spot.leave()
                    freed.append(spot)
            return freed

class ParkingLot:
    def __init__(self, levels: List[Level], rate_calc: Optional[RateCalculator] = None):
        self.levels = levels
        self.rate_calc = rate_calc or RateCalculator()
        self._ticket_seq = itertools.count(1)
        self._tickets_by_plate: Dict[str, ParkingTicket] = {}
        self._tickets_by_id: Dict[int, ParkingTicket] = {}
        self._lot_lock = threading.RLock()

    # -------------------------
    # Public API
    # -------------------------

    def park_vehicle(self, vehicle: Vehicle) -> Optional[ParkingTicket]:
        """Attempt to park a vehicle across levels.

        Returns a ParkingTicket on success, or None if full.
        """
        with self._lot_lock:
            if vehicle.license_plate in self._tickets_by_plate:
                raise ValueError("Vehicle is already parked.")

            placement: Optional[List[ParkingSpot]] = None
            for lvl in self.levels:
                placement = lvl.park(vehicle)
                if placement:
                    break
            if not placement:
                return None

            tid = next(self._ticket_seq)
            ticket = ParkingTicket(
                ticket_id=tid,
                license_plate=vehicle.license_plate,
                spot_ids=[s.id for s in placement],
                entry_ts=time.time(),
            )
            self._tickets_by_plate[vehicle.license_plate] = ticket
            self._tickets_by_id[tid] = ticket
            return ticket

    def unpark_vehicle(self, license_plate: str) -> Optional[ParkingTicket]:
        """Unpark vehicle by plate, compute fee, and mark ticket as PAID (simulation).
        Returns the updated ticket, or None if not found.
        """
        with self._lot_lock:
            ticket = self._tickets_by_plate.get(license_plate)
            if not ticket:
                return None
            # Construct an ephemeral vehicle object for fee calc lookup
            # In a real system, we'd retain the Vehicle instance.
            vehicle = self._infer_vehicle_from_spots(ticket)

            # Free spots
            for (lvl_idx, _, _) in ticket.spot_ids:
                lvl = self.levels[lvl_idx]
                lvl.unpark(vehicle)

            ticket.exit_ts = time.time()
            duration = int(ticket.exit_ts - ticket.entry_ts)
            used_electric = any(self._get_spot_by_id(sid).electric for sid in ticket.spot_ids)
            ticket.amount_cents = self.rate_calc.calculate(vehicle, duration, used_electric)
            ticket.status = PaymentStatus.PAID

            # Remove active mapping (historical tickets could be archived)
            del self._tickets_by_plate[license_plate]
            return ticket

    def get_ticket(self, ticket_id: int) -> Optional[ParkingTicket]:
        return self._tickets_by_id.get(ticket_id)

    def availability(self) -> List[Dict[str, int]]:
        return [lvl.available_summary() for lvl in self.levels]

    # -------------------------
    # Helpers
    # -------------------------

    def _get_spot_by_id(self, sid: Tuple[int, int, int]) -> ParkingSpot:
        lvl_idx, row, num = sid
        return self.levels[lvl_idx].rows[row][num]

    def _infer_vehicle_from_spots(self, ticket: ParkingTicket) -> Vehicle:
        # Infer size from the first spot; infer bus if multiple spots.
        size = self._get_spot_by_id(ticket.spot_ids[0]).size
        is_bus = len(ticket.spot_ids) >= BUS_SPOTS_NEEDED
        electric_used = any(self._get_spot_by_id(s).electric for s in ticket.spot_ids)
        # Note: we cannot reconstruct original plate-specific subclass exactly.
        if is_bus:
            v = Bus(ticket.license_plate)
        elif size == VehicleSize.SMALL:
            v = Motorcycle(ticket.license_plate, electric=electric_used)
        elif size == VehicleSize.MEDIUM:
            v = Car(ticket.license_plate, electric=electric_used)
        else:
            # Large but not bus (e.g., big truck counted as large car)
            v = Vehicle(ticket.license_plate, VehicleSize.LARGE, spots_needed=1, electric=electric_used)
        return v

# -----------------------------
# Factory / Sample Layout Builder
# -----------------------------

def build_level(index: int, layout: List[List[Tuple[VehicleSize, bool]]]) -> Level:
    """Build a Level from a 2D layout where each cell is (size, electric).

    Example layout row:
        [ (VehicleSize.SMALL, False), (VehicleSize.MEDIUM, True), (VehicleSize.LARGE, False) ]
    """
    rows: List[List[ParkingSpot]] = []
    for r, row in enumerate(layout):
        spots_row: List[ParkingSpot] = []
        for c, (size, electric) in enumerate(row):
            spots_row.append(ParkingSpot(level_index=index, row=r, number=c, size=size, electric=electric))
        rows.append(spots_row)
    return Level(index=index, rows=rows)


def sample_parking_lot() -> ParkingLot:
    """Create a small multi-level sample for demo/testing.

    Level 0: one row with [S, S(E), M, M(E), L, L, L, L, L]
    Level 1: two rows to make bus parking easier.
    """
    lvl0 = build_level(0, [[
        (VehicleSize.SMALL, False),
        (VehicleSize.SMALL, True),
        (VehicleSize.MEDIUM, False),
        (VehicleSize.MEDIUM, True),
        (VehicleSize.LARGE, False),
        (VehicleSize.LARGE, False),
        (VehicleSize.LARGE, False),
        (VehicleSize.LARGE, False),
        (VehicleSize.LARGE, False),
    ]])

    lvl1 = build_level(1, [
        [
            (VehicleSize.LARGE, False),
            (VehicleSize.LARGE, False),
            (VehicleSize.LARGE, False),
            (VehicleSize.LARGE, False),
            (VehicleSize.LARGE, False),
            (VehicleSize.MEDIUM, False),
            (VehicleSize.MEDIUM, False),
        ],
        [
            (VehicleSize.SMALL, False),
            (VehicleSize.SMALL, False),
            (VehicleSize.MEDIUM, False),
            (VehicleSize.MEDIUM, False),
            (VehicleSize.LARGE, True),
            (VehicleSize.LARGE, True),
            (VehicleSize.LARGE, False),
            (VehicleSize.LARGE, False),
            (VehicleSize.LARGE, False),
        ],
    ])

    return ParkingLot(levels=[lvl0, lvl1])

# -----------------------------
# Demo / Unit-test-like usage
# -----------------------------

if __name__ == "__main__":
    lot = sample_parking_lot()

    print("Initial availability:")
    print(lot.availability())

    vehicles = [
        Motorcycle("MOTO-001", electric=True),
        Car("CAR-123", electric=True),
        Car("CAR-456"),
        Bus("BUS-999"),
    ]

    tickets = []
    for v in vehicles:
        t = lot.park_vehicle(v)
        if t:
            print(f"Parked {v} -> Ticket {t.ticket_id}, spots={t.spot_ids}")
            tickets.append(t)
        else:
            print(f"No space for {v}")

    print("Availability after parking:")
    print(lot.availability())

    # Simulate some time parked
    time.sleep(1)  # replace with faster mock in real unit tests

    # Unpark
    for v in vehicles:
        tt = lot.unpark_vehicle(v.license_plate)
        if tt:
            print(f"Unparked {v} -> duration={int(tt.exit_ts-tt.entry_ts)}s, amount=${tt.amount_cents/100:.2f}")
        else:
            print(f"Ticket not found for {v}")

    print("Availability at end:")
    print(lot.availability())
