from django import forms

class RechercheForm(forms.Form):
    hotel = forms.ChoiceField(label='Choisir un hotel', choices=[('','Choisir un hotel'), ('Radisson Blu','Radisson Blu'), ('Terrou Bi','Terrou Bi'), ('Pullman','Pullman')], required=False)
    nombre_lit = forms.ChoiceField(label='Nombre de lit', choices=[('','Nombre de lit'), ('1','1'), ('2','2'), ('3','3')], required=False)
    salle_bain = forms.ChoiceField(label='Salle de bain', choices=[('','Salle de bain'), ('1','1'), ('2','2'), ('3','3')], required=False)
