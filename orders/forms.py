from django import forms
from .models import Order



class OrderForm(forms.ModelForm):    
    class Meta:
        model= Order
        fields =['name', 'surname', 'cell_number', 'building', 'room_number',  'additional_notes']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['surname'].widget.attrs['class'] = 'form-control'
        self.fields['surname'].widget.attrs['placeholder'] = 'Surname'
        self.fields['cell_number'].widget.attrs['class'] = 'form-control'
        self.fields['cell_number'].widget.attrs['placeholder'] = 'Number'
        self.fields['building'].widget.attrs['class'] = 'form-control'
        self.fields['building'].widget.attrs['placeholder'] = 'Building'
        self.fields['room_number'].widget.attrs['class'] = 'form-control'
        self.fields['room_number'].widget.attrs['placeholder'] = 'Room Number'
        self.fields['additional_notes'].widget.attrs['class'] = 'form-control'
        self.fields['additional_notes'].widget.attrs['placeholder'] = 'Anything you wish to tell us regarding your order'
        
  