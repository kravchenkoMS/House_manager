from django.urls import reverse
from django.views.generic import UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from pandas import *

from .forms import ResidentForm
from .models import Resident, Flat


class ResidentUpdateView(UpdateView): #todo чи вірні посилання??
    model = Resident
    template_name = 'resident/edit_resident.html'
    form_class = ResidentForm
    success_url = "resident/resident_page.html"


class ResidentDeleteView(DeleteView):
    model = Resident
    success_url = ''
    template_name = 'resident/remove_resident.html'


def show_resident_page(request, resident_id):
    resident = get_object_or_404(Resident, id=resident_id)
    return render(request, "resident/resident_page.html", {'resident':resident})

def show_flats_list_r(request, resident_id):
    resident = get_object_or_404(Resident, id=resident_id)
    flats = Flat.objects.all()
    return render(request, "resident/flats_list_r.html", {"flats":flats, 'resident':resident})

def show_residents_list_r(request, resident_id):
    resident = get_object_or_404(Resident, id=resident_id)
    residents = Resident.objects.all()
    return render(request, "resident/residents_list_r.html", {"residents":residents, 'resident':resident})


def show_choose_table_r(request, resident_id):
    resident = get_object_or_404(Resident, id=resident_id)
    return render(request, "resident/choose_table_r.html", {'resident':resident})


def show_login_r(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        resident = authenticate(request, username=username, password=password)
        if resident is not None:
            login(request, resident)
            return redirect(reverse('resident_page', args=[resident.id]))
        else:
            messages.error(request, "Невірно введені дані. Спробуйте ще раз.")
            return render(request, 'login_r.html')
    return render(request, 'login_r.html')


def show_register_r(request):
    if request.method == 'POST':
        form = ResidentForm(request.POST)
        if form.is_valid():
            resident = form.save(commit=False)
            resident.save()
            return redirect('/resident_page')
    form = ResidentForm()
    data = {'form': form}
    return render(request, "register_resident.html", data)


######## ЕКСПОРТ ТАБЛИЦЬ ########

def export_residents_info(request):
    residents = Resident.objects.all().values(
        'flat', 'name', 'surname', 'phone_number')
    df = DataFrame(residents)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="residents.xlsx"'
    df.to_excel(response, index=False)
    return response


def export_flat_info(request):
    residents = Flat.objects.all().values(
        'number', 'floor', 'residents_amount')
    df = DataFrame(residents)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="flats.xlsx"'
    df.to_excel(response, index=False)
    return response


def export_residents_with_cars(request):
    residents_with_cars = Resident.objects.filter(has_car=True).values(
        'flat', 'name', 'surname', 'phone_number', 'car_model')
    df = DataFrame(residents_with_cars)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="residents_with_cars.xlsx"'
    df.to_excel(response, index=False)
    return response


def export_rented_flats(request):
    bought_flats = Flat.objects.filter(bought=False).values(
        'number', 'floor', 'room_amount', 'residents_amount')
    df = DataFrame(bought_flats)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="rented_flats.xlsx"'
    df.to_excel(response, index=False)
    return response


def export_residents_with_pets(request):
    residents_with_pets = Resident.objects.filter(has_pet=True).values(
        'number', 'name', 'surname', 'phone_number', 'pet_type'
    )
    df = DataFrame(residents_with_pets)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="residents_with_pets.xlsx"'
    df.to_excel(response, index=False)
    return response