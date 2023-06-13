from django import forms

from django import forms

from django import forms

class ReservationForm(forms.Form):
    nom = forms.CharField(label='Nom', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    prenom = forms.CharField(label='Prénom', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    adresse = forms.CharField(label='Adresse', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    telephone = forms.IntegerField(label='Téléphone', widget=forms.NumberInput(attrs={'class': 'form-control mb-3'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control mb-3'}))
