from rest_framework import serializers
from .models import User, Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'roles']
        extra_kwargs = {
            'username': {
                'validators': [serializers.UniqueValidator(queryset=User.objects.all())],
                'required': True,
                'allow_blank': False,
                'min_length': 4,
                'error_messages': {
                    'min_length': 'Не меньше 4 знаков'
                }
            },
            'email': {
                'required': True,
                'allow_blank': False,
                'min_length': 4,
                'error_messages': {
                    'min_length': 'Не меньше 4 знаков'
                }
            },
            'password': {
                'write_only': True,
                'required': True,
                'allow_blank': False
            },
        }

    def create(self, validated_data):
        # Создание пользователя с захэшированным паролем
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        # Обновление пользователя с захэшированным паролем, если он был предоставлен
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])

        instance.save()
        return instance
