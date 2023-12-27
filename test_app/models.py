# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Создание модели Role, аналогичной Role.java
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Создание модели User, расширяющей стандартную модель пользователя Django
class User(AbstractUser):
    # Предполагая, что в User.java были поля, аналогичные следующим:
    roles = models.ManyToManyField(Role, blank=True)

    def __str__(self):
        return self.username
