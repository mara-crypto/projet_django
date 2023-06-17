from django import forms


class ReservationForm(forms.Form):
    nom = forms.CharField(label='Nom', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    prenom = forms.CharField(label='Prénom', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    adresse = forms.CharField(label='Adresse', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    telephone = forms.IntegerField(label='Téléphone', widget=forms.NumberInput(attrs={'class': 'form-control mb-3'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control mb-3'}))


class RechercheForm(forms.Form):
    hotel = forms.ChoiceField(label='Choisir un hotel', choices=[('','Choisir un hotel'), ('Radisson Blu','Radisson Blu'), ('Terrou Bi','Terrou Bi'), ('Pullman','Pullman')], required=False)
    nombre_lit = forms.ChoiceField(label='Nombre de lit', choices=[('','Nombre de lit'), ('1','1'), ('2','2'), ('3','3')], required=False)
    salle_bain = forms.ChoiceField(label='Salle de bain', choices=[('','Salle de bain'), ('1','1'), ('2','2'), ('3','3')], required=False)