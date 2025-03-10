from employee import Employee


def welcome():
    print("WELCOME!")
    print("Submitter 1: Nizar Moklada - Nizar.mok@gmail.com - 205909138")
    print("Submitter 2: Mor Mizrahi - Mizrahi845@gmail.com - 318896719")


def process_command(user):
    parts = user.split()
    if not parts:
        return

    cmd = parts[0]
    if cmd == "welcome":
        welcome()
    elif cmd == "add_employee":
        if len(parts) < 5:
            print(
                "Wrong format for add employee command.\nExpected:\nadd_employee name department age type [manager_id]")
            return
        try:
            name, department, age, emp_type = parts[1:5]
            manager_id = int(parts[5]) if len(parts) > 5 else None
            age = int(age)
            Employee.add_employee(name, department, age, emp_type, manager_id)
        except ValueError:
            print("Wrong format for add employee command.\n\tage must be a number")
    elif cmd == "delete_employee":
        try:
            emp_id = int(parts[1])
            Employee.delete_employee(emp_id)
        except (ValueError, IndexError):
            print("Wrong format for delete employee command.")
    elif cmd == "assign_manager":
        try:
            emp_id, manager_id = int(parts[1]), int(parts[2])
            Employee.assign_manager(emp_id, manager_id)
        except (ValueError, IndexError):
            print("Wrong format for assign manager command.")
    elif cmd == "print_employee":
        try:
            emp_id = int(parts[1])
            Employee.print_employee(emp_id)
        except (ValueError, IndexError):
            print("Wrong format for print employee command.")
    elif cmd == "print_org":
        Employee.print_org()
    elif cmd == "print_dep":
        Employee.print_dep()
    elif cmd == "quit":
        exit()
    else:
        print(f"The command {cmd} is unknown.")


if __name__ == "__main__":
    while True:
        command = input("Please enter a command:\n")
        process_command(command)
