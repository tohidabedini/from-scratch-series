import unittest
from employee import Employee
from unittest.mock import patch


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # once before all
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        # once after all
        print("tearDownClass")

    def setUp(self):
        print("setUp")
        self.emp_1 = Employee("Corey", "Schafer", 50000)
        self.emp_2 = Employee("Tohid", "Abedini", 60000)

    def tearDown(self):
        print("tearDown")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, "Corey.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Tohid.Abedini@email.com")

        self.emp_1.first = "John"
        self.emp_2.first = "Mahdi"

        self.assertEqual(self.emp_1.email, "John.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Mahdi.Abedini@email.com")

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "Corey Schafer")
        self.assertEqual(self.emp_2.fullname, "Tohid Abedini")

        self.emp_1.first = "John"
        self.emp_2.first = "Mahdi"

        self.assertEqual(self.emp_1.fullname, "John Schafer")
        self.assertEqual(self.emp_2.fullname, "Mahdi Abedini")

    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"
            schedule = self.emp_1.monthly_schedule("May")
            mocked_get.assert_called_with("http://company.com/Schafer/May")
            self.assertEqual(schedule, "Success")

            mocked_get.return_value.ok = False
            schedule = self.emp_2.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Abedini/June")
            self.assertEqual(schedule, "Bad Response")


if __name__ == "__main__":
    unittest.main()




