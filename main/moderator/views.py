from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import DeleteView, UpdateView

from resident.models import Resident, Flat
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
    success_url = 'moderator/moderator_page.html'
    template_name = 'moderator/remove_flat.html'

class FlatUpdateView(UpdateView):
    model = Flat
    template_name = 'moderator/edit_flat.html'
    form_class = FlatForm
    success_url = "moderator/moderator_page.html"


def show_login_m(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        moderator = authenticate(request,
                                username=username,
                                password=password)

        if moderator is not None:
            login(request, moderator)
            return redirect("/moderator_page")
        else:
            return render(request, 'login_m.html')
    return render(request, 'login_m.html')

def show_moderator_page(request):
    return render(request, "moderator/moderator_page.html")

def show_choose_table_m(request):
    return render(request, "resident/choose_table_r.html")


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

