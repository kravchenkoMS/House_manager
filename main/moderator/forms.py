from resident.models import Flat
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