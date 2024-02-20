from django.contrib import admin
from .models import User, UserManager, Account, Category, Transaction, Budget, BudgetItem

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Budget)
admin.site.register(BudgetItem)
