from django.contrib.auth.hashers import check_password
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView
from django.http import HttpResponse
from pandas import *

from resident.models import Resident, Flat
from .models import Moderator
from resident.forms import ResidentForm
from .forms import FlatForm


class ResidentDeleteViewModerator(DeleteView):
    model = Resident
    success_url = 'moderator/moderator_page.html'
    template_name = 'moderator/remove_resident_m.html'

class ResidentUpdateViewModerator(UpdateView):
    model = Resident
    template_name = 'moderator/edit_resident_m.html'
    form_class = ResidentForm
    success_url = "moderator/moderator_page.html"

class FlatDeleteView(DeleteView):
    model = Flat
    success_url = reverse_lazy('moderator_page')
    template_name = 'moderator/remove_flat_m.html'

class FlatUpdateView(UpdateView):
    model = Flat
    form_class = FlatForm
    template_name = 'moderator/edit_flat_m.html'
    success_url = '/moderator/flats_list_m'

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return Flat.objects.get(id=id)

def show_login_m(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            moderator = Moderator.objects.get(username=username)
            if check_password(password, moderator.password):
                request.session['moderator_id'] = moderator.id
                return redirect("moderator_page")
            else:
                messages.error(request, "Невірний пароль.")
        except Moderator.DoesNotExist:
            messages.error(request, "Такого модератора не існує.")

    return render(request, 'moderator/login_m.html')


def show_moderator_page(request):
    return render(request, "moderator/moderator_page.html")


def show_choose_table_m(request):
    return render(request, "moderator/choose_table_m.html")


def show_register_resident_m(request):
    if request.method == 'POST':
        form = ResidentForm(request.POST)
        if form.is_valid():
            resident = form.save(commit=False)
            resident.save()
            return redirect('/moderator_page')
    else:
        form = ResidentForm()
    data = {'form': form}
    return render(request, "moderator/register_resident_m.html", data)

def show_register_flat_m(request):
    if request.method == 'POST':
        form = FlatForm(request.POST)
        if form.is_valid():
            flat = form.save(commit=False)
            flat.save()
            return redirect('/moderator/flats_list_m')
    else:
        form = FlatForm()
    data = {'form': form}
    return render(request, "moderator/register_flat_m.html", data)

def show_flats_list_m(request):
    flats = Flat.objects.all()
    return render(request, "moderator/flats_list_m.html", {"flats":flats})

def show_residents_list_m(request):
    residents = Resident.objects.all()
    return render(request, "moderator/residents_list_m.html", {"residents":residents})


###### ТАБЛИЦІ ######

def export_residents_info_m(request):
    residents = Resident.objects.all().values(
        'id', 'flat', 'name', 'surname', 'phone_number', 'has_pet', 'pet_type', 'has_car', 'car_model')
    df = DataFrame(residents)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="residents_m.xlsx"'
    df.to_excel(response, index=False)
    return response


def export_flat_info_m(request):
    residents = Flat.objects.all().values(
        'number', 'floor', 'room_amount', 'bought')
    df = DataFrame(residents)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="flats_m.xlsx"'
    df.to_excel(response, index=False)
    return response


def import_residents_m(request):
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']
        try:
            df = read_excel(excel_file)

            for index, row in df.iterrows():
                flat = Flat.objects.get(number=row['flat__number'])
                Resident.objects.update_or_create(
                    phone_number=row['phone_number'],
                    defaults={
                        'flat': flat,
                        'name': row['name'],
                        'surname': row['surname'],
                        'has_pet': row['has_pet'],
                        'pet_type': row.get('pet_type', ''),  # Використовуємо .get() для необов'язкових полів
                        'has_car': row['has_car'],
                        'car_model': row.get('car_model', '')  # Використовуємо .get() для необов'язкових полів
                    }
                )

            return HttpResponse("<h4>Дані мешканців успішно імпортовано</h4>")
        except Flat.DoesNotExist:
            return HttpResponse("<h4>Помилка імпорту: квартира з таким номером не знайдена</h4>")
        except Exception as e:
            return HttpResponse(f"<h4>Помилка імпорту: {str(e)}</h4>")
    return HttpResponse("<h4>Файл не завантажено</h4>")


def import_flats_m(request):
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']
        try:
            df = read_excel(excel_file)

            for index, row in df.iterrows():
                Flat.objects.update_or_create(
                    number=row['number'],
                    defaults={
                        'floor': row['floor'],
                        'room_amount': row['room_amount'],
                        'bought': row['bought']
                    }
                )

            return HttpResponse("<h4>Дані квартир успішно імпортовано</h4>")
        except Exception as e:
            return HttpResponse(f"<h4>Помилка імпорту: {str(e)}</h4>")
    return HttpResponse("<h4>Файл не завантажено</h4>")