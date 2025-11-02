class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def show_basic_info(self):
        print("\nEmployee Name:", self.name)
        print("Employee ID:", self.emp_id)


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, salary_per_day):
        super().__init__(name, emp_id)
        self.salary_per_day = salary_per_day

    def calculate_salary(self, days):
        total = self.salary_per_day * days
        print("Total Salary:", total)


# ---------- User Input ----------
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
salary_per_day = float(input("Enter Salary per Day: "))
days = int(input("Enter Working Days: "))

emp = FullTimeEmployee(name, emp_id, salary_per_day)
emp.show_basic_info()
emp.calculate_salary(days)
