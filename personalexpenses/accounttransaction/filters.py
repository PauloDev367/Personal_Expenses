import django_filters
from .models import AccountTransaction

class AccountTransactionFilter(django_filters.FilterSet):
    month = django_filters.NumberFilter(field_name="date", lookup_expr="month")
    year = django_filters.NumberFilter(field_name="date", lookup_expr="year")

    class Meta:
        model = AccountTransaction
        fields = ['month', 'year', 'account_type', 'category']
