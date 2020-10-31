from django.urls import path, include
from rest_framework.routers import DefaultRouter

from supplai_api.apps.core.api import views

router = DefaultRouter(trailing_slash=False)
router.register(r'list', views.UserViewSet)

app_name = 'core'

urlpatterns = [
    path('users/', include(router.urls)),
]
