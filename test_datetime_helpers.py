import unittest
from datetime import datetime
from datetime_helpers.helpers import *

class DateTests(unittest.TestCase):

    def test_first_day(self):
        test_date = datetime(2023, 3, 15).date()
        self.assertEqual(first_day(test_date), datetime(2023, 3, 1).date())

    def test_last_day(self):
        test_date = datetime(2023, 3, 15).date()
        self.assertEqual(last_day(test_date), datetime(2023, 3, 31).date())

    def test_last_day_sh(self):
        test_date = datetime(2023, 3, 15).date()
        self.assertEqual(last_day_sh(test_date), datetime(2023, 3, 31).date())

    def test_first_day_of_prev_month(self):
        test_date = datetime(2023, 3, 15).date()
        self.assertEqual(first_day_of_prev_month(test_date), datetime(2023, 2, 1).date())

    def test_last_day_of_prev_month(self):
        test_date = datetime(2023, 3, 15).date()
        self.assertEqual(last_day_of_prev_month(test_date), datetime(2023, 2, 28).date())

    def test_first_day_of_prev_month_sh(self):
        test_date = datetime(2023, 3, 15).date()
        self.assertEqual(first_day_of_prev_month_sh(test_date), datetime(2023, 2, 1).date())

    def test_first_day_of_next_month(self):
        test_date = datetime(2023, 3, 15).date()
        self.assertEqual(first_day_of_next_month(test_date), datetime(2023, 4, 1).date())

    def test_last_day_of_next_month(self):
        test_date = datetime(2023, 3, 15).date()
        self.assertEqual(last_day_of_next_month(test_date), datetime(2023, 4, 30).date())

    def test_last_day_of_next_month_sh(self):
        test_date = datetime(2023, 3, 15).date()
        self.assertEqual(last_day_of_next_month_sh(test_date), datetime(2023, 4, 30).date())


if __name__ == '__main__':
    unittest.main()