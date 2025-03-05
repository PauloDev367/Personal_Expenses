from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Account(Base):
    name = models.CharField(max_length=255)
    balance = models.FloatField()
    user_id = models.ForeignKey(User, related_name='account_user_id', on_delete=models.SET_NULL, null=True)