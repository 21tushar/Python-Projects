import unittest
from unittest.mock import patch
from unitemployee import Employee


# class TestEmployee(unittest.TestCase):
#
#     def setUp(self):
#         self.emp_1 = Employee('Corey', 'Doe', 50000)
#         self.emp_2 = Employee('Jane', 'Doe', 70000)
#
#     def tearDown(self):
#         pass
#
#     def test_email(self):
#         self.assertEqual(self.emp_1.email, 'Corey.Doe@email.com')
#         self.assertEqual(self.emp_2.email, 'Jane.Doe@email.com')
#
#         self.emp_1.first = 'Sarah'
#         self.emp_2.first = 'John'
#
#         self.assertEqual(self.emp_1.email, 'Sarah.Doe@email.com')
#         self.assertEqual(self.emp_2.email, 'John.Doe@email.com')
#
#     def test_fullname(self):
#         self.assertEqual(self.emp_1.fullname, 'Corey Doe')
#         self.assertEqual(self.emp_2.fullname, 'Jane Doe')
#
#         self.emp_1.first = 'Peter'
#         self.emp_2.first = 'Andrew'
#
#         self.assertEqual(self.emp_1.fullname, 'Peter Doe')
#         self.assertEqual(self.emp_2.fullname, 'Andrew Doe')
#
#     def test_apply_raise(self):
#         self.emp_1.apply_raise()
#         self.emp_2.apply_raise()
#
#         self.assertEqual(self.emp_1.pay, 52500)
#         self.assertEqual(self.emp_2.pay, 73500)


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey', 'Doe', 60000)
        self.emp_2 = Employee('Jane', 'Doe', 70000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Corey.Doe@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Doe@email.com')

        self.emp_1.first = 'Carter'
        self.emp_2.first = 'Kelvin'

        self.assertEqual(self.emp_1.email, 'Carter.Doe@email.com')
        self.assertEqual(self.emp_2.email, 'Kelvin.Doe@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Doe')
        self.assertEqual(self.emp_2.fullname, 'Jane Doe')

        self.emp_1.first = 'Alisha'
        self.emp_2.first = 'Justine'

        self.assertEqual(self.emp_1.fullname, 'Alisha Doe')
        self.assertEqual(self.emp_2.fullname, 'Justine Doe')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 63000)
        self.assertEqual(self.emp_2.pay, 73500)

    def test_monthly_schedule(self):
        with patch('unitemployee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Doe/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Doe/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()