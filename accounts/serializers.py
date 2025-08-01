from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as DjoserUserSerializer
from accounts.models import User


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'password')



class CustomUserSerializer(DjoserUserSerializer):
    class Meta(DjoserUserSerializer.Meta):
        fields = [
            'id',
            'email',
            'name',
            'is_active',
            'is_admin',
            'created_at',
            'user_type',
        ]
