from django import forms
from .models import Temple, Pooja

class TempleForm(forms.ModelForm):
    class Meta:
        model = Temple
        fields = ['name', 'location', 'description', 'image', 'contact_number', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Temple Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email (Optional)'}),
        }

class PoojaForm(forms.ModelForm):
    class Meta:
        model = Pooja
        fields = ['temple', 'pooja_name', 'description', 'price', 'image', 'active']
        widgets = {
            'temple': forms.Select(attrs={'class': 'form-select'}),
            'pooja_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pooja Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
