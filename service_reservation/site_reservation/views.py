from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password , check_password
from django.contrib import messages
from datetime import datetime

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
    context={}
    template = loader.get_template("site_reservation/connection.html")
    return HttpResponse(template.render(context,request))

# def reserve_resto(request):
#     context={}
#     template = loader.get_template("site_reservation/reserve_resto.html")
#     return HttpResponse(template.render(context,request))


# import requests
# from datetime import datetime
# def search_results(request):
#     date_debut_str = request.GET.get('date_debut')
#     date_fin_str = request.GET.get('date_fin')

#     if date_debut_str and date_fin_str:
#         date_debut = datetime.strptime(date_debut_str, '%m/%d/%Y').date()
#         date_fin = datetime.strptime(date_fin_str, '%m/%d/%Y').date()

#         # Effectuer une requête HTTP vers l'API 'api-car' avec les dates de début et de fin
#         response = requests.get('https://localhost:8080/api/cars', params={'date_debut': date_debut_str, 'date_fin': date_fin_str})

#         if response.status_code == 200:
#             voitures = response.json()
#             context = {'voitures': voitures, 'date_debut': date_debut, 'date_fin': date_fin}
#             return render(request, 'search_results.html', context)
#         else:
#             return render(request, 'error.html')

#     return render(request, 'search_results.html')



import json

def search_results(request):
    # Charger le fichier JSON
    with open('donnees_voitures.json') as json_file:
        data = json.load(json_file)

    date_debut_str = request.GET.get('date_debut')
    date_fin_str = request.GET.get('date_fin')

    # Accéder aux données pertinentes dans le fichier JSON
    voitures = data['voitures']  # Remplacez 'voitures' par la clé appropriée dans votre fichier JSON

    # Effectuer d'autres opérations avec les données

    context = {'voitures': voitures}
    return render(request, 'search_results.html', context)


def resultat_view(request):
    if request.method == 'GET':
        hotel = request.GET.get('hotel', '')
        nombre_lit = request.GET.get('nombre_lit', '')
        salle_bain = request.GET.get('salle_bain', '')
        date_debut=request.GET.get('date_arrivee')
        date_fin=request.GET.get('date_depart')


        resultats = Suite.objects.filter(hotel__icontains=hotel, nombre_lit=nombre_lit, salle_bain=salle_bain)
        

        context = {'resultats': resultats}
        request.session['hotel']=hotel
        request.session['date_debut']=date_debut
        request.session['date_fin']=date_fin
        return render(request, 'resultat.html', context)
    else:
        return redirect('chambre')

def detail(request, suite_id):
    hotel=request.session.get('hotel')
    date_debut=request.session.get('date_debut')
    date_fin=request.session.get('date_fin')
    suite = Suite.objects.get(id=suite_id)
    print(date_debut)
    request.session['hotel']=hotel
    request.session['suite_id']=suite_id
    request.session['date_debut']=date_debut
    request.session['date_fin']=date_fin
    return render(request, "site_reservation/detail.html", {'suite': suite}) 
   

def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        hashed_password = make_password(password)
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO utilisateur (id,nom, email, password) VALUES (null, %s, %s, %s)", [full_name, email, hashed_password])
                connection.commit()
            return redirect('login')
        except Exception as e:
            print(str(e))
            messages.error(request, 'Error occurred during signup.')
    
    return render(request, "site_reservation/login.html")


from django.urls import reverse

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM utilisateur WHERE email = %s", [email])
            user = cursor.fetchone()
            if user is not None and check_password(password, user[3]):
                request.session['user'] = { 'id' : user[0], 'nom' : user[1], 'email': user[2]}
                redirect_to = request.POST.get('next') or reverse('index')
                return redirect(redirect_to)
            else:
                messages.error(request, 'Invalid credentials')
    
    return render(request, "site_reservation/login.html")

def logout_view(request):
    del request.session['user']
    return redirect('index')


def reserve_resto(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM resto")
        restaurants = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
        context = {"restaurants": restaurants}
        template = loader.get_template("site_reservation/reserve_resto.html")
        return HttpResponse(template.render(context, request))