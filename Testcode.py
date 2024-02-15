import unittest
from Main import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee()
        self.employee.create_employee("Mohamed", 30, 1001, "HR")
        self.employee.create_employee("Hamid", 25, 1002, "Marketing")
        self.employee.create_employee("Ahmed", 35, 1003, "Finance")

    def test_retrieve_employee_found(self):
        employee_id = 1002
        retrieved_employee = self.employee.retrieve_employee(employee_id)
        self.assertIsNotNone(retrieved_employee)
        self.assertEqual(retrieved_employee["name"], "Hamid")
        self.assertEqual(retrieved_employee["age"], 25)
        self.assertEqual(retrieved_employee["department"], "Marketing")

    def test_retrieve_employee_not_found(self):
        employee_id = 9999
        retrieved_employee = self.employee.retrieve_employee(employee_id)
        self.assertIsNone(retrieved_employee)

    def test_delete_employee_found(self):
        employee_id = 1003
        self.assertTrue(self.employee.delete_employee(employee_id))

    def test_delete_employee_not_found(self):
        employee_id = 9999
        self.assertFalse(self.employee.delete_employee(employee_id))

if __name__ == '__main__':
    unittest.main()