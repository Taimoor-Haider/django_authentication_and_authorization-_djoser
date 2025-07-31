from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from accounts.models import User


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'password')