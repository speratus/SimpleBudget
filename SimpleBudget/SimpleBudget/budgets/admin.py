from django.contrib import admin
from SimpleBudget.budgets.models import Expense, Category, Payment, Budget


class ExpenseAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class PaymentAdmin(admin.ModelAdmin):
    pass


class BudgetAdmin(admin.ModelAdmin):
    pass


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Budget, BudgetAdmin)