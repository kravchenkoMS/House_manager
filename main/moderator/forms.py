from resident.models import Flat, Resident
from django.forms import ModelForm, TextInput, CheckboxInput


class FlatForm(ModelForm):
    class Meta:
        model = Flat

        fields = ['number', 'floor', 'room_amount', 'bought',
                  'residents_amount']

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
    class Meta:
        model = Resident

        fields = ['name', 'surname', 'password', 'phone_number',
                  'flat', 'has_pet', 'pet_type',
                  'has_car', 'car_model']

        widgets = {
            "name":TextInput(attrs={
                'class':'form-control'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control'
            }),
            "password": TextInput(attrs={
                'class': 'form-control'
            }),
            "flat": TextInput(attrs={
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