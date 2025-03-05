from rest_framework.routers import SimpleRouter
from .views import AccountTransactionViewSet

router = SimpleRouter()
router.register('', AccountTransactionViewSet)