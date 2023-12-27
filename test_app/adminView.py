from django.http import JsonResponse, Http404
from django.views import View
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from rest_framework.parsers import JSONParser

from .models import User, Role
from .serializers import UserSerializer, RoleSerializer
from .services import UserService
from django.core.exceptions import ObjectDoesNotExist


class AdminView(View):
    userService = UserService()

    def get(self, request):
        # Здесь мы предполагаем, что у вас есть метод в сервисе для получения всех пользователей и ролей
        users = self.userService.get_all_users()
        roles = self.userService.get_all_roles()

        # Преобразование списка пользователей и ролей в сериализованные данные
        users_serializer = UserSerializer(users, many=True)
        roles_serializer = RoleSerializer(roles, many=True)

        # Следует использовать сериализатор для текущего пользователя, если это необходимо
        # current_user = request.user
        # current_user_serializer = UserSerializer(current_user)

        # Возвращаем данные в контексте, чтобы использовать их в шаблоне
        return render(request, 'users.html', {'users': users_serializer.data, 'roles': roles_serializer.data})

    def post(self, request):
        # Десериализация и сохранение нового пользователя
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=201)
        return JsonResponse(user_serializer.errors, status=400)

    def patch(self, request, id):
        # Обновление существующего пользователя
        try:
            user = User.objects.get(pk=id)
        except ObjectDoesNotExist:
            return Http404('User not found')

        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(user, data=user_data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data)
        return JsonResponse(user_serializer.errors, status=400)

    def delete(self, request, id):
        # Удаление пользователя
        try:
            user = User.objects.get(pk=id)
            user.delete()
            return JsonResponse({'message': 'User was deleted successfully!'}, status=204)
        except ObjectDoesNotExist:
            return Http404('User not found')

# Необходимо настроить маршруты в urls.py для обработки этих представлений
