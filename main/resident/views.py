from django.contrib.auth.hashers import check_password, make_password
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from pandas import *

from .forms import ResidentForm
from .models import Resident, Flat


class ResidentUpdateView(UpdateView): #todo чи вірні посилання??
    model = Resident
    template_name = 'edit_resident.html'
    fields = ['username','name', 'surname', 'phone_number',
                  'flat', 'has_pet', 'pet_type',
                  'has_car', 'car_model']
    def get_success_url(self):
        return reverse('resident_page', kwargs={'resident_id': self.object.id})


class ResidentDeleteView(DeleteView):
    model = Resident
    success_url = reverse_lazy('moderator_page')
    template_name = 'remove_resident_m.html'

class FlatUpdateView(UpdateView):
    model = Flat
    fields = ['number', 'floor', 'room_amount', 'bought']
    template_name = 'moderator/edit_flat_m.html'
    success_url = reverse_lazy('flats_list_m')

class FlatDeleteView(DeleteView):
    model = Flat
    success_url = reverse_lazy('moderator_page')
    template_name = 'remove_resident_m.html'

def show_resident_page(request, resident_id):
    resident = get_object_or_404(Resident, id=resident_id)
    return render(request, "resident_page.html", {'resident':resident})

def show_flats_list_r(request, resident_id):
    resident = get_object_or_404(Resident, id=resident_id)
    flats = Flat.objects.all()
    return render(request, "flats_list_r.html", {"flats":flats, 'resident':resident})

def show_residents_list_r(request, resident_id):
    resident = get_object_or_404(Resident, id=resident_id)
    residents = Resident.objects.all()
    return render(request, "residents_list_r.html", {"residents":residents, 'resident':resident})


def show_choose_table_r(request, resident_id):
    resident = get_object_or_404(Resident, id=resident_id)
    return render(request, "choose_table_r.html", {'resident':resident})


def show_login_r(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            resident = Resident.objects.get(username=username)
            if check_password(password, resident.password):
                request.session['resident_id'] = resident.id
                return redirect(reverse('resident_page', args=[resident.id]))
            else:
                messages.error(request, "Невірний пароль.")
        except Resident.DoesNotExist:
            messages.error(request, "Не знайдений користувач.")
            return redirect('register_resident_r')

    return render(request, 'login_r.html')

def show_register_resident_r(request):
    if request.method == 'POST':
        form = ResidentForm(request.POST)
        if form.is_valid():
            resident = form.save(commit=False)

            if isinstance(resident.flat, str):
                try:
                    resident.flat = Flat.objects.get(number=resident.flat)
                except Flat.DoesNotExist:
                    form.add_error('flat', 'Вибрана квартира не існує')
                    return render(request, "register_resident_r.html", {'form': form})

            resident.password = make_password(form.cleaned_data['password'])
            resident.save()
            return redirect('login_r')
    else:
        form = ResidentForm()

    return render(request, "register_resident_r.html", {'form': form})

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
        'number', 'floor', 'room_amount')
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
        'number', 'floor', 'room_amount')
    df = DataFrame(bought_flats)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="rented_flats.xlsx"'
    df.to_excel(response, index=False)
    return response


def export_residents_with_pets(request):
    residents_with_pets = Resident.objects.filter(has_pet=True).values(
        'flat__number', 'name', 'surname', 'phone_number', 'pet_type'
    )
    df = DataFrame(residents_with_pets)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="residents_with_pets.xlsx"'
    df.to_excel(response, index=False)
    return response