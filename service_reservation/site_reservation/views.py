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

def connecter(request):
    context={}
    template = loader.get_template("site_reservation/connection.html")
    return HttpResponse(template.render(context,request))

# def reserve_resto(request):
#     context={}
#     template = loader.get_template("site_reservation/reserve_resto.html")
#     return HttpResponse(template.render(context,request))


# from .models import Resto

# def afficher_emplacements(request):
#     emplacements = Resto.objects.all()
#     return render(request, 'reserve_resto.html', {'reserve_resto': emplacements})


from django.db import connection
def reserve_resto(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM resto")
        restaurants = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
        context = {"restaurants": restaurants}
        template = loader.get_template("site_reservation/reserve_resto.html")
        return HttpResponse(template.render(context, request))
