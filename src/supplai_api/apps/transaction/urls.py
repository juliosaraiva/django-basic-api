from django.urls import path, include
from rest_framework.routers import DefaultRouter

from supplai_api.apps.transaction.api import views


router = DefaultRouter(trailing_slash=False)
router.register(r'new', views.NewTransactionViewSet)
router.register(r'statement', views.TransactionStatementViewSet)
router.register(r'balance', views.TransactionBalanceViewSet)
router.register(r'detail', views.UserDetailViewSet)


app_name = 'transaction'


urlpatterns = [
    path('', include(router.urls)),
]
