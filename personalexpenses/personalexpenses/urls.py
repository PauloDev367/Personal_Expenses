from django.urls import path, include
from account.urls import router as account_router
from accounttransaction.urls import router as account_transaction_router

urlpatterns = [
    path('api/v1/auth/', include('authenticationapp.urls')),
    path('api/v1/accounts/', include(account_router.urls)),
    path('api/v1/transactions/', include(account_transaction_router.urls)),
]
