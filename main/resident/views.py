from django.views.generic import UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login

from .forms import ResidentForm
from .models import Resident


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

def show_choose_table_r(request, resident_id):
    resident = get_object_or_404(Resident, id=resident_id)
    return render(request, "resident/choose_table_r.html", {'resident':resident})

def show_login_r(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        resident = authenticate(request,
                                username=username,
                                password=password)

        if resident is not None:
            login(request, resident)
            return redirect(f"resident_page/{resident.id}")
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
    else:
        form = ResidentForm()
    data = {'form': form}
    return render(request, "register_resident.html", data)
        #todo: перевірити чи працює