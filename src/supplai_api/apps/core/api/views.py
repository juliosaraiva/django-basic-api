from rest_framework import (
    viewsets, mixins, generics, authentication, permissions
)
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.settings import api_settings

from supplai_api.apps.core.models import User
from supplai_api.apps.core.api.serializers import (
    UserSerializer,
    AuthTokenSerializer
)


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user
