from rest_framework import serializers

from supplai_api.apps.core.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone')
