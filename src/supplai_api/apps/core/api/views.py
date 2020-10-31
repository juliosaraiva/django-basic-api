from rest_framework import viewsets, mixins

from supplai_api.apps.core.models import User
from supplai_api.apps.core.api.serializers import UserSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
