# This interview problem consists of four levels or questions. Here are the details for each:
# 1.
# Level 1: Employee Basic Management
# ◦ Create Employee: Implement a function to create an employee with arguments including id, position, and salary. 
# An example would be creating an employee like ("John", "Junior Developer", 100).

# ◦ Register Work Time: Implement a register function that takes an id and a timestamp. 
# An odd number of registrations for a person indicates they are starting work, while an even number indicates they are ending work. 
# For instance, a registration could be ("John", 1).


# ◦ Get Total Work Duration: Implement a get function that takes an id. 
# This function should return the total working duration for that employee. 
# Any work periods where the employee has not yet clocked out (i.e., the last registration is an odd one) should not be included in the calculation. 
# For example, if John registers at times 0, 10, 20, 30, and 50, the result should be 10-0 + 30-20 = 20, 
# because the segment starting at 50 is not yet completed.

# 2.
# Level 2: Top K Employees by Work Duration
# ◦
# Find Longest Working Employees: Implement a method to return the top K individuals with the longest working hours within a specific job level or position.
# ◦
# Performance Note: For "top K" problems, particularly on platforms like Codesignal, directly sorting the relevant data and then returning the first K elements is often sufficient and typically does not lead to timeouts, despite performance requirements.
# 3.
# Level 3: Promotions and Salary Calculation
# ◦
# Promote Employee: Implement a promote method that takes id, newPosition, newSalary, and a timestamp as arguments. A key aspect of this promotion is that it only officially takes effect when the employee first clocks in after the specified timestamp.
# ◦
# Promotion Effect on Top K: It's important to note that when the method from Level 2 (calculating Top K) is used, an employee might have a promotion pending but not yet effective; in such cases, they should still be considered in their previous position for the Top K calculation.
# ◦
# Calculate Total Salary: Implement a calculateSalary method that takes an id. This function should compute the employee's total accumulated salary by multiplying the duration of each work segment by the salary applicable during that specific segment.


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
        Arguments include id, position, and salary [1].
        Example: ("John", "Junior Developer", 100) [1].
        """
        if employee_id in self.employees:
            print(f"Error: Employee '{employee_id}' already exists.")
            return

        self.employees[employee_id] = {
            "position": position,
            "salary": salary,
            "timestamps": [],  # List to store work registration timestamps [1]
            # Future levels (like promotions) might add more attributes here.
        }
        print(f"Employee '{employee_id}' ({position}, ${salary}) created successfully.")

    def register(self, employee_id: str, timestamp: int):
        """
        Implements the 'register' functionality.
        Arguments include id and timestamp [1].
        An odd number of registrations for a person indicates they are starting work.
        An even number of registrations indicates they are ending work [1].
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
        Argument is id [1].
        Returns the total working duration for that employee [1].
        Any work periods where the employee has not yet clocked out (i.e., the last
        registration is an odd one) should not be included in the calculation [1].

        Example: If John registers at times 0, 10, 20, 30, and 50,
        the result should be 10-0 + 30-20 = 20, because the segment starting at 50
        is not yet completed [1].
        """
        if employee_id not in self.employees:
            print(f"Error: Employee '{employee_id}' not found. Cannot get work duration.")
            return 0

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

        print(f"Calculated total work duration for '{employee_id}': {total_duration}")
        return total_duration

# --- Example Usage for Level 1 ---
if __name__ == "__main__":
    system = EmployeeManagementSystem()

    print("--- Testing Level 1: Employee Basic Management ---")

    # 1. Create Employees [1]
    system.create_employee("John", "Junior Developer", 100) # [1]
    system.create_employee("Alice", "Senior Developer", 200)
    system.create_employee("Bob", "Intern", 50)
    system.create_employee("Charlie", "HR", 150)
    print("\n")

    # Attempt to create an existing employee
    system.create_employee("John", "New Position", 120)
    print("\n")

    # 2. Register Work Times [1]
    print("Registering John's work times (example from source):")
    system.register("John", 0)  # Start [1]
    system.register("John", 10) # End   [1]
    system.register("John", 20) # Start [1]
    system.register("John", 30) # End   [1]
    system.register("John", 50) # Start (uncompleted) [1]
    print("\n")

    print("Registering Alice's work times:")
    system.register("Alice", 5)  # Start
    system.register("Alice", 15) # End
    system.register("Alice", 25) # Start
    system.register("Alice", 35) # End
    print("\n")

    print("Registering Bob's work times (uncompleted segment):")
    system.register("Bob", 100) # Start
    print("\n")

    # Attempt to register time for a non-existent employee
    system.register("NonExistent", 1)
    print("\n")

    # 3. Get Total Work Duration [1]
    print("Calculating work durations:")
    john_duration = system.get_total_work_duration("John") # Expected: 10-0 + 30-20 = 20 [1]
    print(f"Result for John: {john_duration}\n")

    alice_duration = system.get_total_work_duration("Alice") # Expected: (15-5) + (35-25) = 10 + 10 = 20
    print(f"Result for Alice: {alice_duration}\n")

    bob_duration = system.get_total_work_duration("Bob") # Expected: 0 (uncompleted segment ignored)
    print(f"Result for Bob: {bob_duration}\n")

    charlie_duration = system.get_total_work_duration("Charlie") # Expected: 0 (no registrations)
    print(f"Result for Charlie: {charlie_duration}\n")

    # Get duration for a non-existent employee
    non_existent_duration = system.get_total_work_duration("NonExistent")
    print(f"Result for NonExistent: {non_existent_duration}\n")
