from django.urls import path, include
from rest_framework.routers import DefaultRouter

from supplai_api.apps.core.api import views

router = DefaultRouter(trailing_slash=False)
router.register(r'list', views.UserViewSet)

app_name = 'core'

urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me')
]
