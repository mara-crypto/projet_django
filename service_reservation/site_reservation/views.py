from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RechercheForm
from .models import Suite, Utilisateur, Reservation_Suite
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def index(request):
    context = {"message": "hello word"}
    return render(request, "site_reservation/index.html", context)

def about(request):
    return render(request, "site_reservation/about.html")

def contact(request):
    return render(request, "site_reservation/contact.html")

def voiture(request):
    return render(request, "site_reservation/voiture.html")

def chambre(request):
    return render(request, "site_reservation/chambre.html")

def restaurant(request):
    return render(request, "site_reservation/restaurant.html")

def detailvoiture(request):
    return render(request, "site_reservation/detailvoiture.html")

def connection(request):
    return render(request, "site_reservation/connection.html")

def detail(request, suite_id):
    suite = Suite.objects.get(id=suite_id)
    return render(request, "site_reservation/detail.html", {'suite': suite})

def recherche_view(request):
    form = RechercheForm()
    context = {'form': form}
    return render(request, 'chambre.html', context)

def resultat_view(request):
    if request.method == 'GET':
        hotel = request.GET.get('hotel', '')
        nombre_lit = request.GET.get('nombre_lit', '')
        salle_bain = request.GET.get('salle_bain', '')

        resultats = Suite.objects.filter(hotel__icontains=hotel, nombre_lit=nombre_lit, salle_bain=salle_bain)

        context = {'resultats': resultats}
        return render(request, 'resultat.html', context)
    else:
        return redirect('chambre')

def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Créer un nouvel utilisateur avec le modèle User de Django
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()

        return redirect('connection')

    return render(request, 'connection.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'connection.html')


@login_required
def reservation_view(request, suite_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            date_arrivee = request.POST.get('date_arrivee')
            date_depart = request.POST.get('date_depart')

            suite = Suite.objects.get(id=suite_id)

            reservation = Reservation_Suite(user_id=request.user.id, date_arrivee=date_arrivee, date_depart=date_depart, suite=suite)
            reservation.save()

            return HttpResponse("Réservation effectuée avec succès")

    return render(request, 'paiement.html', {'suite_id': suite_id})

def paiement(request):
    # Votre logique de traitement pour la page de paiement ici
    # ...

    return render(request, "site_reservation/paiement.html")
