from atexit import register
from django.urls import path
from utilisateurs.views import acceuil, user_login, user_logout, user_register
urlpatterns = [
    path('', acceuil, name="acceuil"),
    path('register', user_register, name="register"),
    path('login', user_login, name="login"),
    path('logout', user_logout, name="logout"),
]