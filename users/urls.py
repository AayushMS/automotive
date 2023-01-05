from django.urls import path, include

from users.views import RegistrationView, Login, logout_view

app_name = 'users'

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]
