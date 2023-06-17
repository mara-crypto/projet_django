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




# def recherche_view(request):
#     if request.method=='GET':
#         form = RechercheForm()
        
#         context = {'form': form}
#     return render(request, 'chambre.html', context)

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


# def reservation_view(request, suite_id):
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             date_arrivee = request.POST.get('date_arrivee')
#             date_depart = request.POST.get('date_depart')

#             suite = Suite.objects.get(id=suite_id)

#             reservation = Reservation_Suite(user_id=request.user.id, date_arrivee=date_arrivee, date_depart=date_depart, suite=suite)
#             reservation.save()

#             return HttpResponse("Réservation effectuée avec succès")

#     return render(request, 'paiement.html', {'suite_id': suite_id})

def paiement(request):
    # Votre logique de traitement pour la page de paiement ici
    # ...
    suite_id=request.session.get('suite_id')
    hotel=request.session.get('hotel')

    date_debut=request.session.get('date_debut')
    date_fin=request.session.get('date_fin')

    date_debut=datetime.strptime(date_debut, '%m/%d/%Y').date()
    date_fin=datetime.strptime(date_fin, '%m/%d/%Y').date()

    date_debut=date_debut.strftime('%Y/%m/%d')
    date_fin=date_fin.strftime('%Y/%m/%d')




    
    user=request.session.get('user')
    user_id=user['id']
    print('Voici id',user_id)
    print(date_debut)
    print('************')
    print(suite_id)
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO reservation_suite (id,utilisateur_id, date_debut, date_fin,id_suite,nom_hotel) VALUES (null, %s, %s, %s, %s, %s)", [user_id, date_debut, date_fin,suite_id,hotel])
            connection.commit()
        #return redirect('paiement')
        return render(request, "site_reservation/paiement.html")
    except Exception as e:
            print(str(e))
            messages.error(request, 'Error occurred during signup.')
            return render(request, "site_reservation/detail.html")



