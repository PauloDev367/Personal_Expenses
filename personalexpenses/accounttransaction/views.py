from rest_framework import viewsets
from .serializers import AccountTransactionSerializer
from .models import AccountTransaction
from rest_framework.permissions import IsAuthenticated

class AccountTransactionViewSet(viewsets.ModelViewSet):
    queryset = AccountTransaction.objects.all()
    serializer_class = AccountTransactionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return AccountTransaction.objects.filter(user=self.request.user)