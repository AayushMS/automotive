"""automotive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vehicle.views import about, list_vehicles, home, create_vehicle

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-our-shop/', about, name='about'),
    path('', home, name='home'),
    path('vehicles/', list_vehicles, name='list-vehicle'),
    path('new-vehicle/', create_vehicle, name='create-vehicle')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)