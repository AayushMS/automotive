from django.http import HttpResponse
from django.shortcuts import render, redirect
from vehicle.models import Vehicle

def about(request):
    return render(request, "about.html")

def home(request):
    return render(request, 'home.html')    

def list_vehicles(request):
    if request.method == 'GET':
        context = {
            'name': 'Harry',
            'all_vehicles': Vehicle.objects.all()
        }
        return render(request, 'list_vehicles.html', context)
    
def create_vehicle(request):
    if request.method == 'POST':
        model = request.POST['model']
        brand = request.POST['brand']
        type = request.POST['type']
        manufactured_date = request.POST['manufactured_date']
        vehicle = Vehicle(
            model = model,
            brand = brand,
            type = type,
            manufactured_date = manufactured_date,
        )
        vehicle.save()
        return redirect('/vehicles/')
    if request.method == 'GET':
        return render(request, 'create_vehicle.html')