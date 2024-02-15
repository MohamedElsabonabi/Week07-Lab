class Employee:
    employees = []

    def create_employee(name, age, employee_id, department):
        employee = {"name": name, "age": age, "id": employee_id, "department": department}
        Employee.employees.append(employee)

    def retrieve_employee(employee_id):
        for employee in Employee.employees:
            if employee["id"] == employee_id:
                return employee
        return None

    def delete_employee(employee_id):
        for employee in Employee.employees:
            if employee["id"] == employee_id:
                Employee.employees.remove(employee)
                return True
        return False

def main():
    employee = Employee()

    employee.create_employee("Mohamed", 30, 1001, "HR")
    employee.create_employee("Hamid", 25, 1002, "Marketing")
    employee.create_employee("Ahmed", 35, 1003, "Finance")

    retrieve_id = 1002
    retrieved_employee = employee.retrieve_employee(retrieve_id)
    if retrieved_employee:
        print("Employee found:")
        print("Name:", retrieved_employee["name"])
        print("Age:", retrieved_employee["age"])
        print("ID:", retrieved_employee["id"])
        print("Department:", retrieved_employee["department"])
    else:
        print("Employee with ID", retrieve_id, "not found.")

    delete_id = 1003
    if employee.delete_employee(delete_id):
        print("Employee with ID", delete_id, "deleted successfully.")
    else:
        print("Employee with ID", delete_id, "not found.")

if __name__ == "__main__":
    main()