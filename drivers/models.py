from django.db import models
from django.contrib.auth.models import User


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="Имя")
    lastname = models.CharField(max_length=50, verbose_name="Фамилия")
    birthday = models.DateField(verbose_name = "Дата рождения")
    age = models.IntegerField(editable=False, verbose_name = "Возраст")
    passport = models.CharField(max_length=11, verbose_name = "Паспорт")
    is_available = models.BooleanField(default=True, verbose_name="Доступность")

    class Meta:
        verbose_name = "Водитель"
        verbose_name_plural = "Водители"

    def __str__(self):
        return " ".join([self.name, self.lastname])