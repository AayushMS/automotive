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
from django.urls import path, include
from vehicle.views import PartDetail, UpdatePart, about, delete_part, list_vehicles, home, \
    create_vehicle, vehicle_detail, vehicle_delete, list_parts, \
        CreatePart, UpdateVehicle

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('about-our-shop/', about, name='about'),
    path('', home, name='home'),
    path('vehicles/', list_vehicles, name='list-vehicle'),
    path('new-vehicle/', create_vehicle, name='create-vehicle'),
    path('vehicles/<int:pk>', vehicle_detail, name='vehicle-detail'),
    path('delete-vehicle/<int:pk>', vehicle_delete, name='delete-vehicle'),
    path('update-vehicle/<int:pk>', UpdateVehicle.as_view(), name='update-vehicle'),
    
    path('parts/', list_parts, name='list-parts'),
    path('new-part/', CreatePart.as_view(), name='create-part'),
    path('part/<int:pk>', PartDetail.as_view(), name='part-detail'),
    path('update-part/<int:pk>', UpdatePart.as_view(), name='update-part'),
    path('delete-part/<int:pk>', delete_part, name='delete-part'),
    
    




]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
