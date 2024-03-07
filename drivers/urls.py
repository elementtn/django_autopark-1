from .views import profile, register, register_done, index, log_in, log_out, select_car, test_fetch
from django.urls import path

app_name = 'drivers'
urlpatterns = [
    path('', index, name='index'),

    path('register/', register, name="register"),
    path('register-done/', register_done, name="register_done"),
    path('login/', log_in, name="login"),
    path('logout/', log_out, name="logout"),

    # path('profile/', profile, name="profile"),

    path('select-car/', select_car, name="select_car"),
    # path('select-car/<int:pk>/', select_car, name="select_car"),
    path('test_fetch/', test_fetch, name="test_fetch"),
    path('profile/<int:pk>/', profile, name="profile")

    
]