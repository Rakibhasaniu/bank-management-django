from django.db import models
from accounts.models import UserBankAccount
# Create your models here.


class Transaction(models.Model):
    account=models.ForeignKey(UserBankAccount,related_name='transaction',on_delete=models.CASCADE)
    amount=models.DecimalField(decimal_places=2,max_digit=12)
    balance_after_transaction=models.DecimalField(decimal_places=2,max_digit=12)
    transaction_type=models.IntegerField(choices='',null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    loan_approve=models.BooleanField(default=False)