from rest_framework import viewsets
from .serializers import AccountTransactionSerializer
from .models import AccountTransaction
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import AccountTransactionFilter

class AccountTransactionViewSet(viewsets.ModelViewSet):
    queryset = AccountTransaction.objects.all()
    serializer_class = AccountTransactionSerializer
    permission_classes = [IsAuthenticated]
    
    # Filters
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['account_type', 'category', 'date']
    search_fields = ['description', 'category']
    ordering_fields = ['amount', 'date']
    filterset_class = AccountTransactionFilter
    
    def get_queryset(self):
        return AccountTransaction.objects.filter(user=self.request.user)