from django.contrib.auth.models import User
from django.db import models
from .enums import car_categories, car_colors
# Create your models here.

class CarBrand(models.Model):
 
    name = models.CharField(max_length=20, verbose_name='Бренд')

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
    
    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='cars', verbose_name='Бренд')
    model = models.CharField(max_length=20, verbose_name='Модель')
    color = models.CharField(max_length=20, choices=car_colors, verbose_name='Цвет')
    power = models.IntegerField(verbose_name='Мощность')
    year = models.IntegerField(verbose_name='Год выпуска')
    image = models.ImageField(upload_to='cars/', blank='True', null='True', verbose_name='Изображение')
    category = models.CharField(max_length=10, choices=car_categories, verbose_name='Класс авто')
    status = models.BooleanField(default=True, verbose_name='Статус машины', editable=False)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return " ".join([self.brand.name, self.model, str(self.year)])
    
class Department(models.Model):
    name=models.CharField(max_length=50, verbose_name='Отдел')

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name

class Position(models.Model):
    name=models.CharField(max_length=50, verbose_name='Должность')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='Имя')
    lastname = models.CharField(max_length=50, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    age = models.IntegerField(editable=False, verbose_name='возраст')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position,on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


    def __str__(self):
        return " ".join([self.name, self.lastname])