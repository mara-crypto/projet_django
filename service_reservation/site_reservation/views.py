from django.shortcuts import render, redirect
from .forms import RechercheForm
from .models import Suite

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
    template = loader.get_template("site_reservation/connecter.html")
    return HttpResponse(template.render(context,request))

def detail(request):
    context={}
    template = loader.get_template("site_reservation/detail.html")
    return HttpResponse(template.render(context,request))



def recherche_view(request):
    form = RechercheForm()
    context = {'form': form}
    return render(request, 'chambre.html', context)

def resultat_view(request):
    if request.method == 'GET':
        hotel = request.GET.get('hotel', '')
        nombre_lit = request.GET.get('nombre_lit', '')
        salle_bain = request.GET.get('salle_bain', '')

        # Effectuer la recherche dans la base de données en utilisant l'ORM de Django
        resultats = Suite.objects.filter(hotel__icontains=hotel, nombre_lit=nombre_lit, salle_bain=salle_bain)

        context = {'resultats': resultats}
        return render(request, 'resultat.html', context)
    else:
        return redirect('chambre')
