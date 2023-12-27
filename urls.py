from django.contrib.auth.views import LoginView
from django.urls import path
from test_app.adminView import AdminView
from test_app.registrationView import RegistrationView
from test_app.userView import UserView
from test_app.registrationView import roles, create_user_role, create_admin_role

urlpatterns = [
    # Путь к представлению администратора
    path('admin/', AdminView.as_view(), name='admin_view'),

    # Пути для регистрации
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),

    # Путь к пользовательскому представлению
    path('user/', UserView.as_view(), name='user_view'),

    # Пути для управления ролями
    path('roles/', roles, name='roles'),
    path('roles/user', create_user_role, name='create_user_role'),
    path('roles/admin', create_admin_role, name='create_admin_role'),
]

# Вам потребуется также импортировать LoginView из django.contrib.auth.views
# или создать свой собственный вид входа, если он еще не существует.
