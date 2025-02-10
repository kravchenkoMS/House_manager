from resident.models import Flat, Resident
from django.forms import *


class FlatForm(ModelForm):
    class Meta:
        model = Flat

        fields = ['number', 'floor', 'room_amount', 'bought', 'residents_amount']

        widgets = {
            "number":TextInput(attrs={
                'class':'form-control'
            }),
            "floor": TextInput(attrs={
                'class': 'form-control'
            }),
            "room_amount": TextInput(attrs={
                'class': 'form-control'
            }),
            "residents_amount": TextInput(attrs={
                'class': 'form-control'
            }),
            "bought": CheckboxInput(attrs={
                'class': 'form-control'
            })
        }

class ResidentForm(ModelForm):
    flat = ModelChoiceField(
        queryset=Flat.objects.all(),
        empty_label="Оберіть квартиру",
        widget=Select(attrs={
            'class':'form-control'
        })
    )

    class Meta:
        model = Resident

        fields = ['username','name', 'surname', 'password', 'phone_number',
                  'flat', 'has_pet', 'pet_type',
                  'has_car', 'car_model']

        widgets = {
            "name":TextInput(attrs={
                'class':'form-control'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control'
            }),
            "username": TextInput(attrs={
                'class': 'form-control'
            }),
            "password": PasswordInput(attrs={
                'class': 'form-control'
            }),
            "phone_number": TextInput(attrs={
                'class': 'form-control'
            }),
            "has_pet": CheckboxInput(attrs={
                'onchange': "togglePetFields()"
            }),
            "has_car": CheckboxInput(attrs={
                'onchange': "toggleCarFields()"
            }),
        }