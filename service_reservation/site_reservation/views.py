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

# def connection(request):
#     context={}
#     template = loader.get_template("site_reservation/connection.html")
#     return HttpResponse(template.render(context,request))


from .models import Hotel

def search_chambre(request):
    hotels = Hotel.objects.all()
    context = {"hotels": hotels}
    template = loader.get_template("site_reservation/search_chambre.html")
    return HttpResponse(template.render(context, request))


from django.db import connection

def recherche_voiture(request):
    with connection.cursor() as cursor :
        cursor.execute("SELECT * FROM site_reservation_voiture")
        voitures = cursor.fetchall()
        context = {"voitures": voitures}
        template = loader.get_template("site_reservation/recherche_voiture.html")
        return HttpResponse(template.render(context, request))
