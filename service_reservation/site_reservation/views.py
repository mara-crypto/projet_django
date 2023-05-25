from django.shortcuts import render


# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    context = {"message": "hello word"}
    template = loader.get_template("site_reservation/index.html")
    return HttpResponse(template.render(context, request))

def about(request):
    context={}
    template = loader.get_template("site_reservation/about.html")
    return HttpResponse(template.render(context,request))

def contact(request):
    context={}
    template = loader.get_template("site_reservation/contact.html")
    return HttpResponse(template.render(context,request))

def voiture(request):
    context={}
    template = loader.get_template("site_reservation/voiture.html")
    return HttpResponse(template.render(context,request))

def chambre(request):
    context={}
    template = loader.get_template("site_reservation/chambre.html")
    return HttpResponse(template.render(context,request))

def restaurant(request):
    context={}
    template = loader.get_template("site_reservation/restaurant.html")
    return HttpResponse(template.render(context,request))

def detailvoiture(request):
    context={}
    template = loader.get_template("site_reservation/detailvoiture.html")
    return HttpResponse(template.render(context,request))

def connection(request):
    context={}
    template = loader.get_template("site_reservation/connection.html")
    return HttpResponse(template.render(context,request))


from .models import Hotel

def search_chambre(request):
    hotels = Hotel.objects.all()
    context = {"hotels": hotels}
    template = loader.get_template("site_reservation/search_chambre.html")
    return HttpResponse(template.render(context, request))


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
