from rest_framework import permissions


class IsBudgetOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsExpensePaymentOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.budget.owner == request.user
