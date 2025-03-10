class Employee:
    employee_counter = 0
    employees = {}
    departments = {}
    CEO = None

    def __init__(self, name, department, age, emp_type, manager_id=None):
        self.id = Employee.employee_counter
        self.name = name
        self.department = department
        self.age = age
        self.emp_type = emp_type
        self.manager_id = manager_id
        self.reporters = []

        Employee.employees[self.id] = self
        Employee.employee_counter += 1

        if department not in Employee.departments:
            Employee.departments[department] = []
        Employee.departments[department].append(self)

        if manager_id is not None and manager_id in Employee.employees:
            Employee.employees[manager_id].reporters.append(self)

    @staticmethod
    def add_employee(name, department, age, emp_type, manager_id=None):
        if emp_type == "CEO":
            if Employee.CEO:
                print("Organization can have only a single CEO")
                return
        elif manager_id is None:
            print("Only CEO can have no manager.")
            return

        if manager_id is not None and manager_id not in Employee.employees:
            print("Manager ID not found.")
            return

        new_employee = Employee(name, department, age, emp_type, manager_id)
        if emp_type == "CEO":
            Employee.CEO = new_employee
            Employee.employee_counter += 1

        print(f"Employee added successfully and was assigned id {new_employee.id}")

    @staticmethod
    def delete_employee(emp_id):
        if emp_id not in Employee.employees:
            print("Employee with this id was not found.")
            return

        employee = Employee.employees[emp_id]

        if employee.reporters:
            print("Employee has reporters = can't delete")
            return

        if employee.manager_id is not None:
            manager = Employee.employees.get(employee.manager_id)
            if manager:
                manager.reporters.remove(employee)

        Employee.departments[employee.department].remove(employee)
        del Employee.employees[emp_id]
        print(f"Employee with id {emp_id} deleted successfully")

    @staticmethod
    def assign_manager(emp_id, manager_id):
        if emp_id not in Employee.employees or manager_id not in Employee.employees:
            print("Employee or Manager ID not found.")
            return
        employee = Employee.employees[emp_id]
        manager = Employee.employees[manager_id]
        if employee.manager_id is not None:
            Employee.employees[employee.manager_id].reporters.remove(employee)
        employee.manager_id = manager_id
        manager.reporters.append(employee)
        print(f"Assigned employee {emp_id} to manager {manager_id}")

    @staticmethod
    def print_employee(emp_id):
        if emp_id not in Employee.employees:
            print("Employee with this id was not found.")
            return
        emp = Employee.employees[emp_id]
        print(
            f"ID: {emp.id}, Name: {emp.name}, Department: {emp.department}, Age: {emp.age}, Type: {emp.emp_type}, Manager ID: {emp.manager_id}")

    @staticmethod
    def print_org():
        def print_hierarchy(employee, level=0):
            if employee.id not in Employee.employees:
                return
            print(
                "\t" * level + f"|--{employee.emp_type} | {employee.department} | {employee.id} | {employee.name} - {employee.age}")
            for rep in employee.reporters:
                print_hierarchy(rep, level + 1)

        if Employee.CEO:
            print_hierarchy(Employee.CEO)

    @staticmethod
    def print_dep():
        total_employees = sum(len(emp_list) for emp_list in Employee.departments.values())
        print(f"Total number of employees = {total_employees}")
        for dep, emp_list in Employee.departments.items():
            print(f"{dep} | number of employees = {len(emp_list)}")
            for emp in emp_list:
                print(f"\t|--{emp.emp_type} | {emp.department} | {emp.id} | {emp.name} - {emp.age}")
