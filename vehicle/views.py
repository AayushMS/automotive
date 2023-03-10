from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from vehicle.forms import BrandForm, PartsForm, VehicleForm
from vehicle.models import Brand, Parts, Vehicle
from django.views import View
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.db.models import Count, F, Q


def about(request):
    return render(request, "about.html")


def home(request):
    vehicles_count = Vehicle.objects.count()
    parts_count = Parts.objects.count()
    brand_count = Brand.objects.count()
    vehicle_count_by_brand = Vehicle.objects.values('brand__name').annotate(total=Count('brand'))
    vehicle_count_by_type = Vehicle.objects.values('type').annotate(total=Count('type'))

    context = {
        'vehicle_count': vehicles_count,
        'parts_count': parts_count,
        'brand_count': brand_count,
        'vehicle_count_by_brand': vehicle_count_by_brand,
        'vehicle_count_by_type': vehicle_count_by_type,
    }
    
    if request.user.is_authenticated:
        total_vehicles_created_by_user = Vehicle.objects.filter(created_by=request.user).count()
        context['total_vehicles_created_by_user'] = total_vehicles_created_by_user
    return render(request, 'home.html', context)


@login_required(login_url='/users/login')
def list_vehicles(request):
    if request.method == 'GET':
        queryset = Vehicle.objects.all().order_by('-updated_date')
        if 'q' in request.GET:
            query_string = request.GET['q']
            queryset = queryset.filter(
                Q(model__icontains=query_string) |
                Q(brand__name__icontains=query_string) |
                Q(type__icontains=query_string)
            )
        context = {
            'all_vehicles': queryset
        }
        return render(request, 'list_vehicles.html', context)


def create_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.created_by = request.user
            vehicle.save()
            messages.success(request, 'Vehicle created successfully')
            return redirect('/vehicles/')
        messages.error(request, 'Failed to create vehicle')
        context = {'form': form}
        return render(request, 'create_vehicle.html', context)
    if request.method == 'GET':
        return render(request, 'create_vehicle.html', {'form': VehicleForm()})


def vehicle_detail(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    context = {
        'vehicle': vehicle,
    }
    return render(request, 'vehicle_detail.html', context)


def vehicle_delete(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    vehicle.delete()
    return redirect('/vehicles/')


class UpdateVehicle(View):

    def get(self, request, pk):
        vehicle = Vehicle.objects.get(id=pk)
        context = {
            'form': VehicleForm(instance=vehicle)
        }
        return render(request, 'update_vehicle.html', context)

    def post(self, request, pk):
        vehicle = Vehicle.objects.get(id=pk)
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            vehicle.save()
            messages.success(request, 'Vehicle updated successfully')
            return redirect(reverse('list-vehicle'))
        messages.error(request, 'Failed to update vehicle')
        return render(request, 'update_vehicle.html', {'form': form})


def list_parts(request):
    if request.method == 'GET':
        context = {
            'all_parts': Parts.objects.all()
        }
        return render(request, 'list_parts.html', context)


class CreatePart(View):
    def get(self, request):
        form = PartsForm()
        context = {
            'form': form,
        }
        return render(request, 'create_part.html', context)

    def post(self, request):
        form = PartsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Part created successfully')
            return redirect('/parts/')
        context = {
            'form': form
        }
        messages.error(request, 'Failed to create part')
        return render(request, 'create_part.html', context)


class PartDetail(LoginRequiredMixin, View):

    login_url = '/users/login'

    def get(self, request, pk):
        context = {
            'part': Parts.objects.get(id=pk)
        }
        return render(request, 'part_detail.html', context)


def delete_part(request, pk):
    if request.method == 'POST':
        part = Parts.objects.get(id=pk)
        part.delete()
        return redirect(reverse('list-parts'))


class UpdatePart(View):

    def get(self, request, pk):
        part = Parts.objects.get(id=pk)
        context = {
            'part': part,
            'form': PartsForm(instance=part)
        }
        return render(request, 'part_update.html', context)

    def post(self, request, pk):
        part = Parts.objects.get(id=pk)
        form = PartsForm(request.POST, instance=part)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated part')
            return redirect(reverse('list-parts'))
        messages.error(request, 'Invalid data')
        context = {'form': form, 'part': part}
        return render(request, 'part_update.html', context)


class ListBrand(ListView):
    model = Brand
    template_name = 'brand/brand_list.html'
    context_object_name = 'brands'
    paginate_by = 4


class CreateBrand(CreateView):
    model = Brand
    template_name = 'brand/brand_create.html'
    form_class = BrandForm
    success_url = reverse_lazy('list-brands')


class DetailBrand(DetailView):
    model = Brand
    template_name = 'brand/brand_detail.html'
    context_object_name = 'brand'


class UpdateBrand(UpdateView):
    model = Brand
    form_class = BrandForm
    context_object_name = 'brand'
    template_name = 'brand/brand_update.html'
    success_url = reverse_lazy('list-brands')


class DeleteBrand(DeleteView):
    model = Brand
    template_name = 'brand/confirm_delete.html'
    success_url = reverse_lazy('list-brands')
