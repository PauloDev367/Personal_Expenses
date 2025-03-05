from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AccountTransactionSerializer
from .models import AccountTransaction

class AccountTransactionViewSet(viewsets.ModelViewSet):
    queryset = AccountTransaction.objects.all()
    serializer_class = AccountTransactionSerializer
    
    def get_queryset(self):
        return AccountTransaction.objects.filter(user=self.request.user)