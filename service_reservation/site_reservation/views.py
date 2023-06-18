from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect, HttpResponse
from django.db import connection
from django.contrib import messages
from .forms import ReservationForm
from .models import Hotel, Suite
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.template import loader
import json
from django.urls import reverse




# Vues pour les pages principales
def index(request):
    return render(request, "site_reservation/index.html")

def about(request):
    return render(request, "site_reservation/about.html")

def contact(request):
    return render(request, "site_reservation/contact.html")

def voiture(request):
    return render(request, "site_reservation/voiture.html")

def chambre(request):
    return render(request, "site_reservation/chambre.html")

def search_chambre(request):
    hotels = Hotel.objects.all()
    context = {"hotels": hotels}
    return render(request, "site_reservation/search_chambre.html", context)

def restaurant(request):
    return render(request, "site_reservation/restaurant.html")

def detailvoiture(request):
    return render(request, "site_reservation/detailvoiture.html")


# Vues pour l'authentification
def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        hashed_password = make_password(password)
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO utilisateur (id,nom, email, PASSWORD) VALUES (null, %s, %s, %s)", [full_name, email, hashed_password])
                connection.commit()
            return redirect('index')
        except Exception as e:
            print(str(e))
            messages.error(request, 'Error occurred during signup.')
    
    return render(request, "site_reservation/login.html")



def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM utilisateur WHERE email = %s", [email])
            user = cursor.fetchone()

            if user is not None and check_password(password, user[3]):
                print(user[3])
                print('\n')
                print('*****************************')
                print(password)
                request.session['user'] = { 'id' : user[0], 'nom' : user[1], 'email': user[2]}
                redirect_to = request.POST.get('next') or reverse('index')
                return redirect(redirect_to)
            else:
                messages.error(request, 'Invalid credentials')
    
    return render(request, "site_reservation/login.html")

def logout_view(request):
    del request.session['user']
    return redirect('index')


# Vues pour les réservations de voitures
def recherche_voiture(request):
    if request.method == 'GET':
        date_debut = request.GET.get('date_debut')
        date_fin = request.GET.get('date_fin')

        date_prise_entre_f = datetime.strptime(date_debut, '%m/%d/%Y').date()
        date_rendu_entre_f = datetime.strptime(date_fin, '%m/%d/%Y').date()

        date_prise_entre = date_prise_entre_f.strftime('%Y/%m/%d')
        date_rendu_entre = date_rendu_entre_f.strftime('%Y/%m/%d')
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM site_reservation_voiture WHERE id NOT IN (SELECT id_voiture FROM reservation_voiture WHERE (%s < date_rendu AND %s > date_reservation) OR (%s > date_rendu AND %s < date_reservation))", [date_prise_entre, date_prise_entre, date_rendu_entre, date_rendu_entre])
            voitures = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
                                                                                                                                       
        context = {"voitures": voitures}
        request.session['date_debut'] = date_prise_entre
        request.session['date_fin'] = date_rendu_entre
        return render(request, "site_reservation/recherche_voiture.html", context)



def detail_voiture(request, voiture_id):
    date_debut = request.session.get('date_debut')
    date_fin = request.session.get('date_fin')
    print(date_debut,date_fin)

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM site_reservation_voiture WHERE site_reservation_voiture.id = %s", [voiture_id])
        voitures = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
    
    context = {"voitures": voitures}
    request.session['date_debut'] = date_debut
    request.session['date_fin'] = date_fin
    request.session['voiture_id'] = voiture_id
    return render(request, "site_reservation/detail_voiture.html", context)




def send_confirmation_email(request):

    date_debut = request.session.get('date_debut')
    date_fin = request.session.get('date_fin')
    print(date_debut, date_fin)

    date_debut = datetime.strptime(date_debut, '%Y/%m/%d').date()
    date_fin = datetime.strptime(date_fin, '%Y/%m/%d').date()

    date_debut = date_debut.strftime('%Y/%m/%d')
    date_fin = date_fin.strftime('%Y/%m/%d')

    user = request.session.get('user')
    user_id = user['id']
    name = user['nom']
    email = user['email']
    voiture_id = request.session.get('voiture_id')

    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO reservation_voiture (id, utilisateur_id, date_reservation, date_rendu, id_voiture) VALUES (null, %s, %s, %s, %s)", [user_id ,date_debut ,date_fin, voiture_id])
        connection.commit()
        reservation_id = cursor.lastrowid


    # Chemin vers le template HTML
    template_path = 'site_reservation/email.html'

    # Contexte de données pour le template
    context = {
        'name': name,
        'reservation_id': reservation_id
    }

    # Charger le contenu du template avec le contexte
    html_content = render_to_string(template_path, context)

    # Créer l'objet EmailMessage pour le message
    email_message = EmailMessage(
        'Confirmation de réservation',
        html_content,
        settings.DEFAULT_FROM_EMAIL,  # Adresse e-mail de l'expéditeur par défaut
        [email] # Liste des adresses e-mail des destinataires
    )
    email_message.content_subtype = 'html'  # Indiquer que le contenu est au format HTML

    # Envoyer l'e-mail
    email_message.send()

    # Afficher une page de confirmation ou rediriger vers une autre URL
    return render(request, 'site_reservation/mesreservation.html')



def paiement(request):
    context ={}
    return render(request, 'site_reservation/paiement.html', context)
            








def mesreservation(request):
    user = request.session.get('user')
    user_id = user['id']
    print(user_id)
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM reservation_voiture WHERE utilisateur_id = %s", [user_id])
        reservations = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]

    context = {'reservations': reservations}
    return render(request, 'site_reservation/mesreservation.html', context)






def reservationVoiture(request):
    date_debut = request.session.get('date_debut')
    date_fin = request.session.get('date_fin')
    voiture_id = request.session.get('voiture_id')

    form = ReservationForm()
    context = {'form': form}
    request.session['date_debut'] = date_debut
    request.session['date_fin'] = date_fin
    request.session['voiture_id'] = voiture_id
    return render(request, "site_reservation/reservationVoiture.html", context)





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
   


def reserve_resto(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM resto")
        restaurants = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
        context = {"restaurants": restaurants}
        template = loader.get_template("site_reservation/reserve_resto.html")
        return HttpResponse(template.render(context, request))