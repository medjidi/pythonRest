from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm
from .models import User, Role
from .services import UserService
from django.contrib import messages
from django.http import HttpResponse

class RegistrationView(View):
    userService = UserService()

    def get(self, request):
        user_form = UserRegistrationForm()
        return render(request, 'registration.html', {'userForm': user_form})

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password')
            email = user_form.cleaned_data.get('email')
            if password != user_form.cleaned_data.get('confirm_password'):
                user_form.add_error('confirm_password', 'Пароли не совпадают')
                return render(request, 'registration.html', {'userForm': user_form})
            if self.userService.username_exists(username):
                user_form.add_error('username', 'Пользователь с таким именем уже существует')
                return render(request, 'registration.html', {'userForm': user_form})
            self.userService.create_user(username, email, password, [])
            return redirect('/login')
        else:
            return render(request, 'registration.html', {'userForm': user_form})

def roles(request):
    return render(request, 'roles.html')

def create_user_role(request):
    user_role, created = Role.objects.get_or_create(name='ROLE_USER')
    if created:
        user_role.save()
    return HttpResponse('Роль USER создана')

def create_admin_role(request):
    admin_role, created = Role.objects.get_or_create(name='ROLE_ADMIN')
    if created:
        admin_role.save()
        if not self.userService.username_exists('admin'):
            user = self.userService.create_user('admin', 'admin@example.com', 'adminpassword', [admin_role])
    return HttpResponse('Роль ADMIN создана и администратор создан, если он не существовал')
