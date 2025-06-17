import collections

class EmployeeManagementSystem:
    def __init__(self):
        """
        Initializes the EmployeeManagementSystem.
        Stores employee data, with each employee identified by their ID.
        """
        # self.employees will store a dictionary where:
        # Key: employee_id (str)
        # Value: A dictionary containing "position", "salary", and "timestamps"
        self.employees = {}

    def create_employee(self, employee_id: str, position: str, salary: int):
        """
        Implements the 'create employee' functionality.
        Arguments include id, position, and salary.
        Example: ("John", "Junior Developer", 100) [1].
        """
        if employee_id in self.employees:
            print(f"Error: Employee '{employee_id}' already exists.")
            return

        self.employees[employee_id] = {
            "position": position,
            "salary": salary,
            "timestamps": [],  # List to store work registration timestamps
            # For Level 3, this would also track historical positions/salaries
        }
        print(f"Employee '{employee_id}' ({position}, ${salary}) created successfully.")

    def register(self, employee_id: str, timestamp: int):
        """
        Implements the 'register' functionality.
        Arguments include id and timestamp.
        An odd number of registrations for a person indicates they are starting work,
        an even number indicates they are ending work [1].
        Example: ("John", 1) [1].
        Timestamps are assumed to be non-decreasing for correct duration calculation.
        """
        if employee_id not in self.employees:
            print(f"Error: Employee '{employee_id}' not found. Cannot register time.")
            return

        self.employees[employee_id]["timestamps"].append(timestamp)
        print(f"Registered timestamp {timestamp} for employee '{employee_id}'.")

    def get_total_work_duration(self, employee_id: str) -> int:
        """
        Implements the 'get' functionality.
        Argument is id.
        Returns the total working duration for that employee.
        Any work periods where the employee has not yet clocked out (i.e., the last
        registration is an odd one) should not be included in the calculation [1].

        Example: If John registers at times 0, 10, 20, 30, and 50,
        the result should be 10-0 + 30-20 = 20, because the segment starting at 50
        is not yet completed [1].
        """
        if employee_id not in self.employees:
            # print(f"Error: Employee '{employee_id}' not found. Cannot get work duration.")
            return 0 # Return 0 for non-existent employees in this context

        timestamps = self.employees[employee_id]["timestamps"]
        total_duration = 0

        # The problem states: "还没下班的时段不计入" (periods not yet ended are not counted) [1].
        # This means if the number of timestamps is odd, the last timestamp represents
        # a start time for which there is no corresponding end time yet.
        # We only consider complete pairs (start, end).
        num_timestamps_to_process = len(timestamps)
        if num_timestamps_to_process % 2 != 0:
            # If the count is odd, the last timestamp is an uncompleted start.
            # We decrement the count to ensure we only process complete pairs.
            num_timestamps_to_process -= 1

        # Iterate through the timestamps in pairs (start_time, end_time)
        # taking two steps at a time.
        for i in range(0, num_timestamps_to_process, 2):
            start_time = timestamps[i]
            end_time = timestamps[i+1]
            total_duration += (end_time - start_time)

        # print(f"Calculated total work duration for '{employee_id}': {total_duration}")
        return total_duration

    def get_top_k_employees_by_work_duration(self, k: int, position_filter: str = None) -> list:
        """
        Implements the Level 2 requirement to return the top K individuals
        with the longest working hours within a specific job level or position [1].

        Args:
            k (int): The number of top employees to return.
            position_filter (str, optional): If provided, filters employees
                                             by this specific position.
                                             If None, considers all positions.

        Returns:
            list: A list of dictionaries, each representing an employee with
                  'id', 'position', and 'total_work_duration',
                  sorted by work duration in descending order.
        """
        eligible_employees_data = []

        for employee_id, data in self.employees.items():
            current_position = data["position"] # This is the current effective position
            
            # Filter by position if a filter is provided [1]
            if position_filter and current_position != position_filter:
                continue # Skip this employee if their position doesn't match the filter

            # Calculate total work duration for the employee
            duration = self.get_total_work_duration(employee_id)
            eligible_employees_data.append({
                "id": employee_id,
                "position": current_position,
                "total_work_duration": duration
            })

        # Sort the employees by their total_work_duration in descending order [1]
        # A simple sort is sufficient for "top K" problems [1].
        eligible_employees_data.sort(key=lambda x: x["total_work_duration"], reverse=True)

        # Return the top K employees
        return eligible_employees_data[:k]


# --- Example Usage for Level 2 ---
if __name__ == "__main__":
    system = EmployeeManagementSystem()

    print("--- Setting up employees and work times for Level 2 testing ---")
    system.create_employee("John", "Junior Developer", 100)
    system.create_employee("Alice", "Senior Developer", 200)
    system.create_employee("Bob", "Junior Developer", 120)
    system.create_employee("Charlie", "Senior Developer", 210)
    system.create_employee("David", "Junior Developer", 110)
    system.create_employee("Eve", "Intern", 50)
    print("\n")

    # Register work times for various employees
    # John: (0-10) + (20-30) = 20
    system.register("John", 0)
    system.register("John", 10)
    system.register("John", 20)
    system.register("John", 30)
    system.register("John", 50) # Uncompleted, not counted
    print("\n")

    # Alice: (5-15) + (25-40) = 10 + 15 = 25
    system.register("Alice", 5)
    system.register("Alice", 15)
    system.register("Alice", 25)
    system.register("Alice", 40)
    print("\n")

    # Bob: (0-5) = 5 (only one segment)
    system.register("Bob", 0)
    system.register("Bob", 5)
    print("\n")

    # Charlie: (100-150) = 50
    system.register("Charlie", 100)
    system.register("Charlie", 150)
    print("\n")

    # David: No work registered yet = 0
    # Eve: (10-20) + (30-45) + (50-60) = 10 + 15 + 10 = 35
    system.register("Eve", 10)
    system.register("Eve", 20)
    system.register("Eve", 30)
    system.register("Eve", 45)
    system.register("Eve", 50)
    system.register("Eve", 60)
    print("\n")


    print("--- Testing Level 2: Top K Employees by Work Duration ---")

    # Test 1: Get top 3 employees overall (no position filter)
    print("Top 3 employees overall:")
    top_3_overall = system.get_top_k_employees_by_work_duration(3)
    for emp in top_3_overall:
        print(f"ID: {emp['id']}, Position: {emp['position']}, Work Duration: {emp['total_work_duration']}")
    # Expected order: Eve (35), Charlie (50), Alice (25), John (20), Bob (5), David (0)
    # Expected Top 3: Eve, Charlie, Alice (or Charlie, Eve, Alice if Charlie has longer)
    # Let's recheck the durations:
    # John: 20
    # Alice: 25
    # Bob: 5
    # Charlie: 50
    # David: 0
    # Eve: 35
    # Correct order by duration (desc): Charlie (50), Eve (35), Alice (25), John (20), Bob (5), David (0)
    # Top 3 should be: Charlie, Eve, Alice
    print("-" * 30, "\n")

    # Test 2: Get top 2 "Junior Developer" employees
    print("Top 2 'Junior Developer' employees:")
    top_2_junior_devs = system.get_top_k_employees_by_work_duration(2, "Junior Developer")
    for emp in top_2_junior_devs:
        print(f"ID: {emp['id']}, Position: {emp['position']}, Work Duration: {emp['total_work_duration']}")
    # Junior Developers: John (20), Bob (5), David (0)
    # Expected Top 2: John, Bob
    print("-" * 30, "\n")

    # Test 3: Get top 1 "Senior Developer" employee
    print("Top 1 'Senior Developer' employee:")
    top_1_senior_dev = system.get_top_k_employees_by_work_duration(1, "Senior Developer")
    for emp in top_1_senior_dev:
        print(f"ID: {emp['id']}, Position: {emp['position']}, Work Duration: {emp['total_work_duration']}")
    # Senior Developers: Alice (25), Charlie (50)
    # Expected Top 1: Charlie
    print("-" * 30, "\n")

    # Test 4: Get top 5 employees from a non-existent position
    print("Top 5 'NonExistent' employees (should be empty):")
    top_5_non_existent = system.get_top_k_employees_by_work_duration(5, "NonExistent")
    if not top_5_non_existent:
        print("No employees found for 'NonExistent' position.")
    else:
        for emp in top_5_non_existent:
            print(f"ID: {emp['id']}, Position: {emp['position']}, Work Duration: {emp['total_work_duration']}")
    print("-" * 30, "\n")
