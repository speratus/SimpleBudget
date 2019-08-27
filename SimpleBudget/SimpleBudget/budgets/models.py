from django.db import models
from django.contrib.auth.models import User
from .validators import validate_budget_period


class Budget(models.Model):
    name = models.CharField(max_length=512)
    creation_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets', default=1)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name + ": " + self.owner.username


class Category(models.Model):
    EXPENSE = 'e'
    PAYMENT = 'p'
    BOTH = 'b'
    TYPES  = [
        (EXPENSE, 'Expense'),
        (PAYMENT, 'Payment'),
        (BOTH, 'Both')
    ]
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=1, choices=TYPES)


class Expense(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField(blank=True)
    amount = models.FloatField()
    date = models.DateField()
    period = models.CharField(max_length=127, validators=[validate_budget_period])
    payee = models.CharField(max_length=512, blank=True)
    budget = models.ForeignKey('Budget', on_delete=models.CASCADE, default=1, related_name='expenses')
    categories = models.ManyToManyField(Category, null=True, blank=True)

    def __str__(self):
        return self.name + ': ' + str(self.amount)

    def clean(self):
        validate_budget_period(self.period)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.full_clean()
        return super(Expense, self).save(force_insert, force_update, using, update_fields)


class Payment(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField(blank=True)
    amount = models.FloatField()
    date = models.DateField()
    period = models.CharField(max_length=127, validators=[validate_budget_period])
    origin = models.CharField(max_length=512, blank=True)
    budget = models.ForeignKey('Budget', on_delete=models.CASCADE, related_name='payments')
    categories = models.ManyToManyField(Category, null=True, blank=True)

    def __str__(self):
        return f'{self.name}: {self.amount}'
