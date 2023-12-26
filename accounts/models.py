from django.db import models
from django.contrib.auth.models import User
# Create your models here.
ACCOUNT_TYPE = (
    ('Savings','Savings'),
    ('Current','Current'),
)
class UserBankAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete = models.CASCADE)
    account_type= models.CharField(max_length=50, choices=ACCOUNT_TYPE)
    account_no= models.IntegerField(unique=True)
    birth_date=models.DateField(null=True, blank=True)
