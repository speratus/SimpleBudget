from django.test import TestCase
from .validators import validate_budget_period
from .models import Budget, Expense, Payment
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError


class ExpenseTestCases(TestCase):
    def setUp(self) -> None:
        user = User.objects.create_user('joe', email='hellother@obiwan.com', password='imlame')
        budget = Budget.objects.create(name='My budget',
                                       creation_date='2019-05-03',
                                       owner=user,
                                       description='The budget of champions.'
                                       )
        Expense.objects.create(name='Water park visit',
                               amount=30.00,
                               period='1-monthly',
                               payee='Super awesome Water parks',
                               description='I will go to the water park.',
                               date='2019-06-04',
                               budget=budget
                               )
        Payment.objects.create(name='Paycheck',
                               amount=4000.0,
                               period='1-monthly',
                               description='Where the Mullah comes from',
                               date='2017-01-12',
                               origin='The big boss fom up top in HR.',
                               budget=budget
                               )

    def test_proper_str_formation(self):
        budget = Budget.objects.get(pk=1)
        expense = Expense.objects.get(pk=1)
        payment = Payment.objects.get(pk=1)

        self.assertEquals(budget.__str__(), 'My budget: joe', 'The budget was not created properly.')
        self.assertEquals(expense.__str__(), 'Water park visit: 30.0', 'The expense was not create properly.')
        self.assertEquals(payment.__str__(), 'Paycheck: 4000.0', 'The string function on payment is not workng properly.')


class BudgetPeriodValidatorTestCase(TestCase):
    valid_cases = [
        '1-daily',
        '1-onetime',
        '1-annually',
        '5-quarterly',
        '7-weekly',
        '3-annually',
        '10-monthly',
        '19-weekly',
        '99-daily'
                   ]
    invalid_cases = [
        '0.4-daily',
        '0-weekly',
        'ad-annually',
        '100-weekly',
        '4.6-quarterly',
        '-31-daily',
        'whoot-quarterly',
        '59-zoobly',
        '5-onetime',
        '03-monthly',
    ]

    def test_budget_period_validator(self):
        for c in self.valid_cases:
            self.assertEquals(validate_budget_period(c), None, f'failed on {c}')

    def test_budget_period_validator_fail(self):
        for c in self.invalid_cases:
            self.assertRaises(ValidationError, validate_budget_period, c)

    def test_validator_in_expense_model_creation_invalid(self):
        user = User.objects.create(username='joe', email='hithere@obiwan.com', password='imlame')
        budget = Budget.objects.create(name='My Budget',
                                       creation_date='2019-04-13',
                                       owner=user,
                                       )
        for c in self.invalid_cases:
            self.assertRaises(Exception, Expense.objects.create,
                              name=c + '1',
                              amount=15.0,
                              date='2014-05-06',
                              period=c,
                              budget=budget
                              )
