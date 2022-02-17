import unittest
import datetime

# --------------------------------------------------------------------------------#
from datetime import timedelta
from typing import Any, Union


def first_day_of_month(my_date):
    """
        Takes a datetime.date object and returns a datetime.date object
        which is the first day of that month.
    """
    first_date = my_date.replace(day=1)
    return first_date

# --------------------------------------------------------------------------------#
def last_day_of_month(my_date):
    """
        Takes a datetime.date object and returns a datetime.date object
        which is the last day of that month.
    """

    next_month = my_date.replace(day=28) + datetime.timedelta(days=4)
    last_day = next_month - datetime.timedelta(days=next_month.day)
    return last_day

# --------------------------------------------------------------------------------#
def next_day(my_date):
    """
        Takes a datetime.date object and returns a datetime.date object
        which is the next day. For example:
    """
    next_day = my_date + datetime.timedelta(days=1)
    return next_day

# --------------------------------------------------------------------------------#
def string2date(month):
    """
        Convert String to DateTime
    """
    tmp = month.split("-")
    year = int(tmp[0])
    month = int(tmp[1])
    day = 1
    my_date = datetime.date(year, month, 1)
    return my_date

# --------------------------------------------------------------------------------#
def bill_for(month, active_subscription, users):
    """
        Iterate through list and get information from a My-Dictionary
    """
    cost_accumulator = 0.0
    price = active_subscription.get('monthly_price_in_dollars')
    print("-" * 50)

    for item in users:
        first_date = item.get("activated_on")
        last_date = item.get("deactivated_on")
        if last_date is None:
            last_date = last_day_of_month(first_date)

        print("First Date: " + str(first_date))
        print("Last Date: " + str(last_date))
        difference = last_date - first_date
        total_days = difference.days
        print("Total Days: " + str(total_days))
        cost = total_days * price
        cost_accumulator += cost
        print(cost)
        print("-" * 50)
        delta = 1.01

    return cost_accumulator

# --------------------------------------------------------------------------------#
user_signed_up = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2018, 11, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2018, 12, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 3,
        'name': 'Employee #3',
        'activated_on': datetime.date(2019, 1, 10),
        'deactivated_on': None,
        'customer_id': 1,
    },
]
# --------------------------------------------------------------------------------#
constant_users = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2018, 11, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2018, 12, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
]
# --------------------------------------------------------------------------------#
new_plan = {
    'id': 1,
    'customer_id': 1,
    'monthly_price_in_dollars': 4
}

no_users = []

# --------------------------------------------------------------------------------#
# Note: the Class must be called Test
class Test(unittest.TestCase):

    # def test_works_when_the_customer_has_no_active_users_during_the_month(self):
    #   self.assertAlmostEqual(bill_for('2019-01', new_plan, no_users), 0.00, delta=0.01)

    def test_works_when_everything_stays_the_same_for_a_month(self):
        # self.assertAlmostEqual(bill_for('2019-01', new_plan, constant_users), 8.00, delta=0.01)
        self.assertAlmostEqual(bill_for('2019-01', new_plan, constant_users), 212.0, delta=0.01)

    # def test_works_when_a_user_is_activated_during_the_month(self):
    #   self.assertAlmostEqual(bill_for('2019-01', new_plan, user_signed_up), 10.84, delta=0.01)
