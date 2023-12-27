from django.contrib.auth.hashers import make_password
from .models import User, Role

class UserService:

    def create_user(self, username, email, password, roles):
        user = User(username=username, email=email)
        user.password = make_password(password)
        user.save()
        user.roles.set(roles)  # Используем set() вместо add() для установки связей M2M
        return user

    def get_user(self, username):
        return User.objects.get(username=username)

    def delete_user(self, username):
        user = self.get_user(username)
        user.delete()

    def get_all_users(self):
        return User.objects.all()

    def get_all_roles(self):
        return Role.objects.all()

    def update_user(self, user, data):
        # Обновляем данные пользователя
        for field, value in data.items():
            setattr(user, field, value)
        if 'password' in data:
            user.password = make_password(data['password'])
        user.save()
        return user

    def save_user(self, user_data):
        # Сохраняем нового пользователя или обновляем существующего
        user, created = User.objects.update_or_create(
            defaults=user_data,
            username=user_data.get('username')
        )
        return user

    def delete_user_by_id(self, user_id):
        # Удаление пользователя по ID
        try:
            user = User.objects.get(pk=user_id)
            user.delete()
            return True
        except User.DoesNotExist:
            return False
