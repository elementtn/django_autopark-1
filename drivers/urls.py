from django.urls import path
from .views import register, register_done, index, log_in, log_out, select_car, test_fetch, profile, refuse_car


app_name = "drivers"

urlpatterns = [
    path('', index, name='index'),


    path('register/', register, name="register"),
    path('login/', log_in, name="login"),
    path('register-done/', register_done, name="register_done"),
    path('logout/', log_out, name="logout"),

    path('profile/<int:pk>',profile, name="profile"),
    path('select-car/', select_car, name="select_car" ),

    path('refuse-car/', refuse_car, name="refuse_car"),

    path('test-fetch', test_fetch, name="test_fetch"),

    ]

