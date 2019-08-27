from django.contrib.auth.models import User, Group
from rest_framework import serializers

from SimpleBudget.budgets.models import Budget, Expense, Payment


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    budget = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='budget-detail')

    class Meta:
        model = Expense
        fields = ['name', 'amount', 'description', 'date', 'budget', 'period', 'payee']


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ['name', 'amount', 'description', 'date', 'budget', 'period', 'origin']


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Budget
        fields = ['name', 'owner', 'creation_date', 'description']


class ExtendedBudgetSerializer(BudgetSerializer):
    expenses = ExpenseSerializer(many=True, read_only=True)
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = Budget
        fields = ['name', 'owner', 'creation_date', 'description', 'payments', 'expenses']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
