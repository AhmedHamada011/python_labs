from Employee import Employee
from Manager import Manager


def menu():
    flag = True
    while flag:
        print("Please select an operation:")
        print("Add new employee: ae")
        print("Add new manager: am")
        print("List all employees: le")
        print("List all managers: lm")

        print("Exit program: q")
        key = input().lower()
        if key == "ae":
            data = get_employee_data()
            Employee(*data)
        elif key == "am":
            data = get_manager_data()
            Manager(*data)
        elif key == "le":
            Employee.list_employees()
        elif key == "lm":
            Manager.list_employees()
        elif key == "q":
            flag = False


def get_employee_data(type="employee"):
    first_name = input(f"\nEnter {type} first_name: ")
    last_name = input(f"\nEnter {type} last_name: ")
    age = int(input(f"\nEnter {type} age: "))
    department = input(f"\nEnter {type} department: ")
    salary = float(input(f"\nEnter {type} salary: "))
    return [first_name, last_name, age, department, salary]


def get_manager_data():
    data = get_employee_data("manager")
    managed_department = input("\nEnter manager managed_department: ")
    data.append(managed_department)
    return data


menu()
