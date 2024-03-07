from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    lastname = models.CharField(max_length=50, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    age = models.IntegerField(editable=False, verbose_name='возраст')
    phone = models.CharField(max_length=20,verbose_name='Номер Телефона')
    email = models.EmailField(verbose_name='Почта')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return " ".join([self.name, self.lastname])

