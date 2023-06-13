from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.db import connection
from django.template import loader
from django.http import HttpResponse
from django.db import connection
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .forms import ReservationForm
from .models import Hotel


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



def search_chambre(request):
    hotels = Hotel.objects.all()
    context = {"hotels": hotels}
    template = loader.get_template("site_reservation/search_chambre.html")
    return HttpResponse(template.render(context, request))


def restaurant(request):
    context={}
    template = loader.get_template("site_reservation/restaurant.html")
    return HttpResponse(template.render(context,request))

def detailvoiture(request):
    context={}
    template = loader.get_template("site_reservation/detailvoiture.html")
    return HttpResponse(template.render(context,request))






from django.db import connection
from django.contrib.auth.hashers import make_password, check_password

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
                cursor.close()
                return redirect('index')
        except Exception as e:
            
            print(str(e))
            context = {}
            template = loader.get_template("site_reservation/login.html")
            return HttpResponse(template.render(context, request))

            

    #     # Autres actions ou redirection après l'inscription réussie
    #     context = {}
    #     template = loader.get_template("site_reservation/index.html")
    #     return HttpResponse(template.render(context, request))

    # context = {}
    # template = loader.get_template("site_reservation/login.html")
    # return HttpResponse(template.render(context, request))

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
                
                # Créez une session de connexion pour l'utilisateur
                request.session['user'] = { 'id' : user[0], 'nom' : user[1], 'email': user[2]}

                # Obtenir l'URL de la page précédente
                redirect_to = request.POST.get('next') or reverse('index')
                return redirect(redirect_to)
            else:
                # Gérer les erreurs de connexion
                context = {'error': 'Invalid credentials'}
                template = loader.get_template("site_reservation/login.html")
                return HttpResponse(template.render(context, request))
    
    context = {}
    template = loader.get_template("site_reservation/login.html")
    return HttpResponse(template.render(context, request))


from django.shortcuts import redirect

def logout_view(request):
    # Supprimer les clés de session de l'utilisateur
    del request.session['user']
    # Rediriger vers la page d'accueil ou une autre page appropriée
    return redirect('index')







def recherche_voiture(request):
    if request.method == 'GET':
        date_debut = request.GET.get('date_debut')
        date_fin = request.GET.get('date_fin')

        # Convertir les valeurs de date en objets datetime appropriés
        date_prise_entre = datetime.strptime(date_debut, '%m/%d/%Y').date()
        date_rendu_entre = datetime.strptime(date_fin, '%m/%d/%Y').date()

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM site_reservation_voiture WHERE id NOT IN (SELECT id_voiture FROM reservation_voiture WHERE (date_reservation <= %s AND date_rendu >= %s) OR (date_reservation <= %s AND date_rendu <= %s) OR (date_reservation >= %s AND date_rendu <= %s))", [date_prise_entre, date_rendu_entre, date_prise_entre, date_rendu_entre, date_prise_entre, date_rendu_entre])
            voitures = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]

        context = {"voitures": voitures}
        template = loader.get_template("site_reservation/recherche_voiture.html")
        return HttpResponse(template.render(context, request))
    else :
        None



def detail_voiture(request, voiture_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM site_reservation_voiture WHERE site_reservation_voiture.id = %s", [voiture_id])
        voitures = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
    
    context = {"voitures": voitures}
    template = loader.get_template("site_reservation/detail_voiture.html")
    return HttpResponse(template.render(context, request))


def reservationVoiture(request):
    form = ReservationForm()
    context = {'form': form}
    template = loader.get_template("site_reservation/reservationVoiture.html")
    return HttpResponse(template.render(context, request))




def confirmationVoiture(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Traitez les données de réservation de voiture ici
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            adresse = form.cleaned_data['adresse']
            telephone = form.cleaned_data['telephone']
            email = form.cleaned_data['email']

            # Effectuez les actions nécessaires avec les données de réservation

            # Redirigez vers la page de confirmation après la réservation
            context ={}
            return render(request, 'site_reservation/confirmationVoiture.html', context)
    else:
        form = None

    context = {'form': form}
    return render(request, 'site_reservation/reservationVoiture.html', context)





















































# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# # import mysql.connector
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages

# # Définition de la fonction pour la réservation de voiture
# @login_required
# def reservationVoiture(request):
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             # Récupérer les données du formulaire
#             nom = form.cleaned_data['nom']
#             prenom = form.cleaned_data['prenom']
#             email = form.cleaned_data['email']
#             adresse = form.cleaned_data['adresse']
#             telephone = form.cleaned_data['telephone']

#             # Étape 2 : Vérifier si l'utilisateur est déjà inscrit
#             user_exists = request.user.is_authenticated
#             if user_exists:
#                 # L'utilisateur est déjà inscrit et connecté
#                 # user_id = request.user.id
#                 None
#             else:
#                 # L'utilisateur n'est pas inscrit ou non connecté
#                 # Rediriger vers la page de connexion
#                 return redirect('connecter')  # Remplacez 'connecter' par le nom de votre vue de connexion

#             # Étape 3 : Insérer les informations de réservation dans la table "reservation_voiture"
#             conn = mysql.connector.connect(user='modou', password='modou', host='127.0.0.1', database='gestion_reservation')
#             cursor = conn.cursor()
#             insert_query = "INSERT INTO reservation_voiture (nom, prenom, adresse, telephone, email) VALUES (%s, %s, %s, %s, %s)"
#             cursor.execute(insert_query, [nom, prenom, adresse, telephone, email])
#             reservation_id = cursor.lastrowid
#             conn.commit()
#             cursor.close()
#             conn.close()

#             # Étape 6 : Envoyer un e-mail de confirmation avec le reçu en pièce jointe
#             send_confirmation_email(email)

#             # Afficher un message de succès
#             messages.success(request, "Votre réservation a été effectuée avec succès!")

#             # Rediriger vers la page de confirmation
#             return redirect('confirmation')

#     else:
#         form = ReservationForm()

#     return render(request, 'reservationVoiture.html', {'form': form})

# # Définition de la fonction pour envoyer un e-mail de confirmation
# def send_confirmation_email(email):
#     # Paramètres SMTP pour l'envoi d'e-mails
#     smtp_host = 'smtp.example.com'
#     smtp_port = 587
#     smtp_username = 'your_username'
#     smtp_password = 'your_password'

#     # Créer l'objet MIMEMultipart pour le message
#     msg = MIMEMultipart()
#     msg['From'] = 'your_email@example.com'
#     msg['To'] = email
#     msg['Subject'] = 'Confirmation de réservation'

#     # Contenu du message
#     message = "Votre réservation a été confirmée. Merci!"

#     # Ajouter le contenu du message
#     msg.attach(MIMEText(message, 'plain'))

#     # Établir une connexion SMTP et envoyer l'e-mail
#     try:
#         smtp_server = smtplib.SMTP(smtp_host, smtp_port)
#         smtp_server.starttls()
#         smtp_server.login(smtp_username, smtp_password)
#         smtp_server.send_message(msg)
#         smtp_server.quit()
#         print("E-mail de confirmation envoyé avec succès")
#     except Exception as e:
#         print("Erreur lors de l'envoi de l'e-mail de confirmation:", str(e))






































# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import mysql.connector
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# # from mysql.connector import connection
# from .forms import ReservationForm

# @login_required
# def reservationVoiture(request):
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             # Récupérer les données du formulaire
#             nom = form.cleaned_data['nom']
#             prenom = form.cleaned_data['prenom']
#             email = form.cleaned_data['email']
#             adresse = form.cleaned_data['adresse']
#             telephone = form.cleaned_data['telephone']

#             # Étape 2 : Vérifier si l'utilisateur est déjà inscrit
#             user_exists = request.user.is_authenticated
#             if user_exists:
#                 # L'utilisateur est déjà inscrit et connecté
#                 # user_id = request.user.id
#                 None
#             else:
#                 # L'utilisateur n'est pas inscrit ou non connecté
#                 # Rediriger vers la page de connexion
#                 return redirect('connecter')  # Remplacez 'login' par le nom de votre vue de connexion

#             # Étape 3 : Insérer les informations de réservation dans la table "reservation_voiture"
#             with mysql.connector.connect(user='your_username', password='your_password', host='your_host', database='your_database') as conn:
#                 cursor = conn.cursor()
#                 cursor.execute("INSERT INTO reservation_voiture (nom, prenom, adresse, telephone, email) VALUES (%s, %s, %s, %s, %s)",
#                             [nom, prenom, adresse, telephone, email])
#                 reservation_id = cursor.lastrowid
#                 conn.commit()
#                 cursor.close()


#             # Étape 6 : Envoyer un e-mail de confirmation avec le reçu en pièce jointe
#             send_confirmation_email(email)

#             # Afficher un message de succès
#             messages.success(request, "Votre réservation a été effectuée avec succès!")

#             # Rediriger vers la page de confirmation
#             return redirect('confirmation')

#     else:
#         form = ReservationForm()

#     return render(request, 'reservationVoiture.html', {'form': form})


# # Définition de la fonction pour envoyer un e-mail de confirmation
# def send_confirmation_email(email):
#     # Paramètres SMTP pour l'envoi d'e-mails
#     smtp_host = 'smtp.example.com'
#     smtp_port = 587
#     smtp_username = 'your_username'
#     smtp_password = 'your_password'

#     # Créer l'objet MIMEMultipart pour le message
#     msg = MIMEMultipart()
#     msg['From'] = 'your_email@example.com'
#     msg['To'] = email
#     msg['Subject'] = 'Confirmation de réservation'

#     # Contenu du message
#     message = "Votre réservation a été confirmée. Merci!"

#     # Ajouter le contenu du message
#     msg.attach(MIMEText(message, 'plain'))

#     # Établir une connexion SMTP et envoyer l'e-mail
#     try:
#         smtp_server = smtplib.SMTP(smtp_host, smtp_port)
#         smtp_server.starttls()
#         smtp_server.login(smtp_username, smtp_password)
#         smtp_server.send_message(msg)
#         smtp_server.quit()
#         print("E-mail de confirmation envoyé avec succès")
#     except Exception as e:
#         print("Erreur lors de l'envoi de l'e-mail de confirmation:", str(e))
