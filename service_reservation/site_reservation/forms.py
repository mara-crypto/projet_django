from django import forms

class ReservationForm(forms.Form):
    nom = forms.CharField(label='Nom', max_length=20)
    prenom = forms.CharField(label='Prénom', max_length=50)
    adresse = forms.CharField(label='Adresse', max_length=100)
    telephone = forms.IntegerField(label='Téléphone')
    email = forms.EmailField(label='Email')
