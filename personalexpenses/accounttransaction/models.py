from django.db import models
from django.contrib.auth.models import User
from account.models import Account

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class AccountTransactionType(models.TextChoices):
    EXPENSE = 'expense', 'Expense'
    INCOME = 'income', 'Income'

class AccountTransaction(Base):
    type_choices = ('expense', 'income')
    user = models.ForeignKey(User, related_name='account_transactions_user_id', on_delete=models.SET_NULL, null=True)
    account = models.ForeignKey(Account, related_name='account_transactions_account_id', on_delete=models.SET_NULL, null=True)
    amount = models.FloatField()
    account_type = models.CharField(
        max_length=30,
        choices=AccountTransactionType.choices
    )
    category = models.CharField(max_length=150)
    date = models.DateTimeField()
    description = models.TextField()