from django.urls import path, include
from account.urls import router as account_router

urlpatterns = [
    path('api/v1/auth/', include('authenticationapp.urls')),
    path('api/v1/accounts/', include(account_router.urls))
]
