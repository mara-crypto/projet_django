from django.shortcuts import render,redirect
from django.contrib.auth.models import User

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
    if request.method == 'POST':
        
    # Récupérer les données de la requête POST
        name = request.POST.get('name')
        email = request.POST.get('email')
        mot_de_passe = request.POST.get('password')
        # print("**************************")
        # print(email)
        # print(mot_de_passe)
        
        # Creer un nouveau utilisateur
        user = User(username=name,email=email,password=mot_de_passe)
        user.save()
        return redirect('restaurant')

    context={}
    template = loader.get_template("site_reservation/connecter.html")
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
    if request.method == 'POST':
        type_repas = request.POST.get('type_repas')
        nb_enfants = request.POST.get('nb_enfants')
        nb_adultes = request.POST.get('nb_adultes')

        print(type_repas)
        print(nb_enfants)
        print(nb_adultes)
        
        # Faites quelque chose avec les valeurs récupérées
        # ...
        return render(request, 'success.html')
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM resto")
        restaurants = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
        context = {"restaurants": restaurants}
        template = loader.get_template("site_reservation/reserve_resto.html")
        return HttpResponse(template.render(context, request))

    # return render(request, 'site_reservation/reserve_resto.html')

# def reserve_resto(request):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM resto")
#         restaurants = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
#         context = {"restaurants": restaurants}
#         template = loader.get_template("site_reservation/reserve_resto.html")
#         return HttpResponse(template.render(context, request))


