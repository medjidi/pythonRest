from django.contrib import admin
from .models import User, Role

# Определение класса администратора для модели Role
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Поля, которые будут отображаться в списке
    search_fields = ('name',)  # Поля, по которым можно выполнять поиск

# Определение класса администратора для модели User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    filter_horizontal = ('roles',)  # Удобное редактирование ManyToMany полей
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Roles', {'fields': ('roles',)}),
    )
