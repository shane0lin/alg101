import collections

class EmployeeManagementSystem:
    def __init__(self):
        """
        Initializes the EmployeeManagementSystem.
        Stores employee data, with each employee identified by their ID.
        """
        self.employees = {}

    def create_employee(self, employee_id: str, position: str, salary: int):
        """
        Implements the 'create employee' functionality [2].
        Arguments include id, position, and salary. Example: ("John","Junior Developer", 100) [2].
        """
        if employee_id in self.employees:
            print(f"Error: Employee '{employee_id}' already exists.")
            return

        self.employees[employee_id] = {
            "timestamps": [],  # List to store work registration timestamps [2]
            "promotions_queue": collections.deque(), # Stores (promo_timestamp, new_position, new_salary)
                                                     # for promotions yet to be applied [1].
            "position_salary_history": [
                # Stores periods of effective position and salary.
                # Format: (effective_start_timestamp, effective_end_timestamp, position, salary)
                # effective_end_timestamp is float('inf') for the current ongoing period.
                # Assumed effective from a conceptual time 0 [1].
                (0, float('inf'), position, salary)
            ]
        }
        print(f"Employee '{employee_id}' ({position}, ${salary}) created successfully.")

    def register(self, employee_id: str, timestamp: int):
        """
        Implements the 'register' functionality [2].
        Arguments include id and timestamp [2].
        An odd number of registrations indicates starting work, an even number indicates ending work [2].
        Promotions become effective at the first clock-in at or after their scheduled timestamp [1].
        """
        if employee_id not in self.employees:
            print(f"Error: Employee '{employee_id}' not found. Cannot register time.")
            return

        employee_data = self.employees[employee_id]
        employee_data["timestamps"].append(timestamp)
        # Ensure timestamps are sorted, as `get_total_work_duration` relies on pairs [2].
        # Problem assumes non-decreasing timestamps, but sorting adds robustness.
        employee_data["timestamps"].sort()

        # Process pending promotions based on this timestamp [1]
        latest_eligible_promotion_details = None
        
        # Temporary queue to hold promotions that are not yet eligible (promo_ts > current_timestamp)
        temp_promotions_queue = collections.deque() 

        # Iterate through the promotions_queue.
        # Since the queue is sorted by promo_ts, we can process them sequentially.
        while employee_data["promotions_queue"]:
            promo_ts, new_pos, new_sal = employee_data["promotions_queue"].popleft()
            if promo_ts <= timestamp:
                # This promotion is eligible to take effect with this register call.
                # If multiple promotions become eligible at the same 'register' timestamp,
                # the one with the latest `promo_ts` is the one whose attributes will be
                # set as effective *from this `timestamp`*.
                latest_eligible_promotion_details = (new_pos, new_sal)
            else:
                # This promotion is not yet eligible, put it back to the temporary queue
                temp_promotions_queue.append((promo_ts, new_pos, new_sal))
        
        # Restore the promotions_queue with remaining (unapplied) promotions
        employee_data["promotions_queue"] = temp_promotions_queue

        if latest_eligible_promotion_details:
            # A promotion (or multiple) just became effective at `timestamp` [1].
            # We need to close the previous effective period in position_salary_history
            # and start a new one with the newly effective position/salary.
            
            # Get the last (current) state in history.
            old_start_ts, old_end_ts, old_pos, old_sal = employee_data["position_salary_history"][-1]
            
            # Update its end_timestamp to the current timestamp, as the old state ends here.
            employee_data["position_salary_history"][-1] = (old_start_ts, timestamp, old_pos, old_sal)
            
            # Add the new state that starts at the current timestamp, with new position/salary.
            new_pos, new_sal = latest_eligible_promotion_details
            employee_data["position_salary_history"].append((timestamp, float('inf'), new_pos, new_sal))

        print(f"Registered timestamp {timestamp} for employee '{employee_id}'.")

    def promote(self, employee_id: str, newPosition: str, newSalary: int, timestamp: int):
        """
        Implements the 'promote' method [1].
        Arguments: id, newPosition, newSalary, timestamp.
        Promotion becomes effective when the employee first clocks in after this timestamp [1].
        """
        if employee_id not in self.employees:
            print(f"Error: Employee '{employee_id}' not found. Cannot promote.")
            return

        employee_data = self.employees[employee_id]
        
        # Add the promotion to the queue. Keep the queue sorted by timestamp for correct processing.
        temp_list = list(employee_data["promotions_queue"])
        temp_list.append((timestamp, newPosition, newSalary))
        temp_list.sort(key=lambda x: x) # Sort by promo_ts
        employee_data["promotions_queue"] = collections.deque(temp_list)
        
        print(f"Promotion for '{employee_id}' to {newPosition} with salary ${newSalary} scheduled for timestamp {timestamp}.")

    def get_total_work_duration(self, employee_id: str) -> int:
        """
        Implements the 'get' functionality [2].
        Argument is id [2].
        Returns the total working duration for that employee [2].
        Work periods where the employee has not yet clocked out (last registration is odd) are not included [2].
        """
        if employee_id not in self.employees:
            return 0

        timestamps = self.employees[employee_id]["timestamps"]
        total_duration = 0

        # Only consider complete pairs (start, end) of registrations [2].
        num_timestamps_to_process = len(timestamps)
        if num_timestamps_to_process % 2 != 0:
            num_timestamps_to_process -= 1

        for i in range(0, num_timestamps_to_process, 2):
            start_time = timestamps[i]
            end_time = timestamps[i+1]
            total_duration += (end_time - start_time)
        return total_duration

    def _get_current_effective_position(self, employee_id: str) -> str:
        """
        Helper to get the current effective position of an employee [1].
        This is used for filtering in get_top_k_employees_by_work_duration.
        It reflects the position from the latest actual effective state in position_salary_history.
        """
        if employee_id not in self.employees:
            return None
        # The current effective position is the one from the last entry in position_salary_history.
        # Format: (start_ts, end_ts, position, salary)
        return self.employees[employee_id]["position_salary_history"][-1][1]

    def get_top_k_employees_by_work_duration(self, k: int, position_filter: str = None) -> list:
        """
        Implements the Level 2 requirement to return the top K individuals
        with the longest working hours within a specific job level or position [2].
        A simple sort is sufficient for "top K" problems [2].
        Note: An employee with a pending promotion (not yet effective) still counts in their previous position [1].
        """
        eligible_employees_data = []

        for employee_id, data in self.employees.items():
            # Use the helper to get the currently effective position for filtering [1].
            current_effective_position = self._get_current_effective_position(employee_id)
            
            if position_filter and current_effective_position != position_filter:
                continue

            duration = self.get_total_work_duration(employee_id)
            eligible_employees_data.append({
                "id": employee_id,
                "position": current_effective_position, # Use the effective position [1]
                "total_work_duration": duration
            })

        # Sort the employees by their total_work_duration in descending order [2].
        eligible_employees_data.sort(key=lambda x: x["total_work_duration"], reverse=True)

        return eligible_employees_data[:k]

    def calculate_salary(self, employee_id: str) -> int:
        """
        Implements the 'calculateSalary' functionality [1].
        Calculates the total salary for an employee.
        Each segment of work time is multiplied by the salary effective during that specific period [1].
        """
        if employee_id not in self.employees:
            print(f"Error: Employee '{employee_id}' not found. Cannot calculate salary.")
            return 0

        employee_data = self.employees[employee_id]
        timestamps = employee_data["timestamps"]
        position_salary_history = employee_data["position_salary_history"]
        total_salary = 0

        # Only consider complete work segments (paired clock-in/out) [2].
        num_timestamps_to_process = len(timestamps)
        if num_timestamps_to_process % 2 != 0:
            num_timestamps_to_process -= 1

        # Iterate through each completed work segment (e.g., (0, 10), (20, 30))
        for i in range(0, num_timestamps_to_process, 2):
            work_segment_start = timestamps[i]
            work_segment_end = timestamps[i+1]

            # Iterate through the employee's position/salary history to find
            # how this work segment overlaps with different salary periods [1].
            for eff_start, eff_end, pos, sal in position_salary_history:
                # Calculate the actual overlap period between the work segment
                # and the current effective salary period.
                overlap_start = max(work_segment_start, eff_start)
                overlap_end = min(work_segment_end, eff_end)

                # If there's a valid overlap (overlap_start < overlap_end),
                # calculate the duration of this overlap and add to total salary.
                if overlap_start < overlap_end:
                    duration_in_overlap = overlap_end - overlap_start
                    total_salary += duration_in_overlap * sal
        
        return total_salary


# --- Example Usage for Level 3 ---
if __name__ == "__main__":
    system = EmployeeManagementSystem()

    print("--- Setting up employees and work times for Level 3 testing ---")
    system.create_employee("John", "Junior Developer", 10) # Salary $10/hour
    system.create_employee("Alice", "Intern", 5) # Salary $5/hour
    print("\n")

    print("--- Testing Promotion (Level 3) ---")
    # Promote John to Senior Dev, $20/hour, effective from timestamp 50
    system.promote("John", "Senior Developer", 20, 50)
    # Promote Alice to Junior Dev, $12/hour, effective from timestamp 70
    system.promote("Alice", "Junior Developer", 12, 70)
    # Promote John again to Lead Dev, $30/hour, effective from timestamp 90 (later than first promo)
    system.promote("John", "Lead Developer", 30, 90)
    print("-" * 30, "\n")


    print("--- Registering work times and observing promotion effects ---")
    # John's work:
    # 0-10: Junior Dev (10 hours * $10)
    system.register("John", 0)
    system.register("John", 10)
    print(f"John's current position: {system._get_current_effective_position('John')}") # Should be Junior Dev
    print(f"John's total work duration: {system.get_total_work_duration('John')}")
    print(f"John's calculated salary: {system.calculate_salary('John')}") # Expected: 10 * 10 = 100
    print("\n")

    # John's next clock-in is at 60, which is >= promo_ts 50. Promotion to Senior Dev takes effect.
    # 60-80: Senior Dev (20 hours * $20)
    system.register("John", 60) # Promotion to Senior Dev (ts 50) becomes effective at ts 60
    system.register("John", 80)
    print(f"John's current position: {system._get_current_effective_position('John')}") # Should be Senior Dev
    print(f"John's total work duration: {system.get_total_work_duration('John')}") # Expected: 10 + 20 = 30
    print(f"John's calculated salary: {system.calculate_salary('John')}") # Expected: (10*10) + (20*20) = 100 + 400 = 500
    print("\n")

    # John's next clock-in is at 100, which is >= promo_ts 90. Promotion to Lead Dev takes effect.
    # 100-110: Lead Dev (10 hours * $30)
    system.register("John", 100) # Promotion to Lead Dev (ts 90) becomes effective at ts 100
    system.register("John", 110)
    print(f"John's current position: {system._get_current_effective_position('John')}") # Should be Lead Dev
    print(f"John's total work duration: {system.get_total_work_duration('John')}") # Expected: 30 + 10 = 40
    print(f"John's calculated salary: {system.calculate_salary('John')}") # Expected: 500 + (10*30) = 500 + 300 = 800
    print("\n")

    # Alice's work:
    # 0-20: Intern (20 hours * $5)
    system.register("Alice", 0)
    system.register("Alice", 20)
    print(f"Alice's current position: {system._get_current_effective_position('Alice')}") # Should be Intern
    print(f"Alice's total work duration: {system.get_total_work_duration('Alice')}")
    print(f"Alice's calculated salary: {system.calculate_salary('Alice')}") # Expected: 20 * 5 = 100
    print("\n")

    # Alice's next clock-in is at 80, which is >= promo_ts 70. Promotion to Junior Dev takes effect.
    # 80-90: Junior Dev (10 hours * $12)
    system.register("Alice", 80) # Promotion to Junior Developer (ts 70) becomes effective at ts 80
    system.register("Alice", 90)
    print(f"Alice's current position: {system._get_current_effective_position('Alice')}") # Should be Junior Developer
    print(f"Alice's total work duration: {system.get_total_work_duration('Alice')}") # Expected: 20 + 10 = 30
    print(f"Alice's calculated salary: {system.calculate_salary('Alice')}") # Expected: (20*5) + (10*12) = 100 + 120 = 220
    print("\n")

    print("--- Testing Level 2 (Top K) with Level 3 Promotions ---")
    # This demonstrates that 'top K' correctly uses the *currently effective* position.
    
    # John's current effective position is 'Lead Developer'.
    # Alice's current effective position is 'Junior Developer'.

    print("Top 5 employees overall (should reflect current positions):")
    top_5_overall = system.get_top_k_employees_by_work_duration(5)
    for emp in top_5_overall:
        print(f"ID: {emp['id']}, Position: {emp['position']}, Work Duration: {emp['total_work_duration']}")
    # Expected: John (40h), Alice (30h)
    print("-" * 30, "\n")

    print("Top 1 'Lead Developer' employee:")
    top_1_lead_dev = system.get_top_k_employees_by_work_duration(1, "Lead Developer")
    for emp in top_1_lead_dev:
        print(f"ID: {emp['id']}, Position: {emp['position']}, Work Duration: {emp['total_work_duration']}")
    # Expected: John
    print("-" * 30, "\n")

    print("Top 1 'Junior Developer' employee:")
    top_1_junior_dev = system.get_top_k_employees_by_work_duration(1, "Junior Developer")
    for emp in top_1_junior_dev:
        print(f"ID: {emp['id']}, Position: {emp['position']}, Work Duration: {emp['total_work_duration']}")
    # Expected: Alice
    print("-" * 30, "\n")

    print("Top 1 'Intern' employee (Alice is no longer an Intern):")
    top_1_intern = system.get_top_k_employees_by_work_duration(1, "Intern")
    if not top_1_intern:
        print("No employees found for 'Intern' position (Alice was promoted).")
    else:
        for emp in top_1_intern:
            print(f"ID: {emp['id']}, Position: {emp['position']}, Work Duration: {emp['total_work_duration']}")
    print("-" * 30, "\n")
