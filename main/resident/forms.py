from .models import Resident
from django.forms import ModelForm, TextInput, CheckboxInput

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