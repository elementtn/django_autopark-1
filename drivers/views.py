from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import RegistrationForm, DriverForm
from AutoparkProject.utils import calculate_age
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from AutoparkProject.settings import LOGIN_REDIRECT_URL
from employees.models import Car


def register(request):
    if request.method == "POST":
        reg_form = RegistrationForm(request.POST)
        driver_form = DriverForm(request.POST)

        if reg_form.is_valid() and driver_form.is_valid():
            user = reg_form.save()
            driver = driver_form.save(commit=False)
            driver.user = user
            driver.age = calculate_age(driver.birthday)
            driver.save()
            # return redirect("driver_profile")
            # return render(request, "autopark/driver_profile.html", {"driver": driver})
            return register_done(request, new_user=driver)
    

    # для метода GET
    reg_form = RegistrationForm()
    driver_form = DriverForm()
    context = {"reg_form": reg_form, "driver_form": driver_form}
    
    return render(request, "drivers/register.html", context=context)


# будет вызываться при успешной регистрации
def register_done(request, new_user):
    context = {"driver": new_user, 'title': 'Успешно'}
    return render(request, 'drivers/register_done.html', context=context)


def index(request):
    title = 'Главная страница'
    context = {'title': title}
    return render(request, 'drivers/index.html', context=context)


def log_in(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                url = request.GET.get('next', LOGIN_REDIRECT_URL)
                return redirect(url)
        
    return render(request, 'drivers/login.html', {'form': form, 'title': 'Вход'})


def log_out(request):
    logout(request)
    url = LOGIN_REDIRECT_URL
    return redirect(url)


def select_car(request, pk=None):
    if request.method == "GET":
        title = 'Choose a car'
        cars = Car.objects.filter(status=True)
        context ={'title': title, 'cars': cars}
    if pk is not None:
        print(pk)
        car = Car.objects.get(pk=pk)
        car.status = False
        car.save()
        return redirect("drivers:index")

    return render(request, 'drivers/select_car.html', context=context)


def test_fetch(request):
    car = request.POST.get('carId')
    return JsonResponse(car)
