from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .services import UserService

class UserView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        user = request.user
        return render(request, 'user.html', {'admin': user})

# В urls.py добавьте следующий путь для этого представления:
# path('user/', UserView.as_view(), name='user_view'),
