from django.contrib.auth.models import User, Group

from SimpleBudget.budgets.serializers import UserSerializer, GroupSerializer, ExtendedBudgetSerializer, PaymentSerializer
from SimpleBudget.budgets.serializers import ExpenseSerializer
from SimpleBudget.budgets.models import Budget, Payment, Expense
from SimpleBudget.budgets.permissions import IsBudgetOwner, IsExpensePaymentOwner

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = ExtendedBudgetSerializer
    permission_classes = [IsAuthenticated, IsBudgetOwner]

    def list(self, request, *args, **kwargs):
        bs = Budget.objects.filter(owner=request.user)
        data = {'budget_number': bs.count()}
        return Response(data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    permission_classes = [IsAuthenticated, IsExpensePaymentOwner]

    def list(self, request):
        bs = Budget.objects.filter(owner=request.user)
        count = 0

        for b in bs:
            count += b.payments.count()

        data = {'payment_number': count}
        return Response(data)


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    permission_classes = [IsAuthenticated, IsExpensePaymentOwner]

    def list(self, request, *args, **kwargs):
        bs = Budget.objects.filter(owner=request.user)
        count = 0
        for b in bs:
            count += b.expense.count()
        data = {'expense_number': count}
        return Response(data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view(['GET'])
def root(request):
    data = {'budget_number': Budget.objects.count(),
            'user_number': User.objects.count()
            }
    return Response(data)
