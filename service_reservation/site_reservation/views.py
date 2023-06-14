# from django.http import HttpResponse
# from django.template import loader
from datetime import datetime
# from django.db import connection
# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import ReservationForm
# from .models import Hotel


# # Create your views here.

# def index(request):
#     context = {}
#     template = loader.get_template("site_reservation/index.html")
#     return HttpResponse(template.render(context, request))

# def about(request):
#     context={}
#     template = loader.get_template("site_reservation/about.html")
#     return HttpResponse(template.render(context,request))

# def contact(request):
#     context={}
#     template = loader.get_template("site_reservation/contact.html")
#     return HttpResponse(template.render(context,request))

# def voiture(request):
#     context={}
#     template = loader.get_template("site_reservation/voiture.html")
#     return HttpResponse(template.render(context,request))

# def chambre(request):
#     context={}
#     template = loader.get_template("site_reservation/chambre.html")
#     return HttpResponse(template.render(context,request))


# def search_chambre(request):
#     hotels = Hotel.objects.all()
#     context = {"hotels": hotels}
#     template = loader.get_template("site_reservation/search_chambre.html")
#     return HttpResponse(template.render(context, request))


# def restaurant(request):
#     context={}
#     template = loader.get_template("site_reservation/restaurant.html")
#     return HttpResponse(template.render(context,request))

# def detailvoiture(request):
#     context={}
#     template = loader.get_template("site_reservation/detailvoiture.html")
#     return HttpResponse(template.render(context,request))






# from django.db import connection
from django.contrib.auth.hashers import make_password, check_password

# def signup(request):
#     if request.method == 'POST':
#         full_name = request.POST.get('full_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         hashed_password = make_password(password)
#         try:
#             with connection.cursor() as cursor:
#                 cursor.execute("INSERT INTO utilisateur (id,nom, email, PASSWORD) VALUES (null, %s, %s, %s)", [full_name, email, hashed_password])
#                 connection.commit()
#                 cursor.close()
#                 return redirect('index')
#         except Exception as e:
            
#             print(str(e))
#             context = {}
#             template = loader.get_template("site_reservation/login.html")
#             return HttpResponse(template.render(context, request))

            

#     #     # Autres actions ou redirection après l'inscription réussie
#     #     context = {}
#     #     template = loader.get_template("site_reservation/index.html")
#     #     return HttpResponse(template.render(context, request))

#     # context = {}
#     # template = loader.get_template("site_reservation/login.html")
#     # return HttpResponse(template.render(context, request))

# from django.urls import reverse

# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(password)

#         with connection.cursor() as cursor:
#             cursor.execute("SELECT * FROM utilisateur WHERE email = %s", [email])
#             user = cursor.fetchone()
#             if user is not None and check_password(password, user[3]):
                
#                 # Créez une session de connexion pour l'utilisateur
#                 request.session['user'] = { 'id' : user[0], 'nom' : user[1], 'email': user[2]}

#                 # Obtenir l'URL de la page précédente
#                 redirect_to = request.POST.get('next') or reverse('index')
#                 return redirect(redirect_to)
#             else:
#                 # Gérer les erreurs de connexion
#                 context = {'error': 'Invalid credentials'}
#                 template = loader.get_template("site_reservation/login.html")
#                 return HttpResponse(template.render(context, request))
    
#     context = {}
#     template = loader.get_template("site_reservation/login.html")
#     return HttpResponse(template.render(context, request))


# from django.shortcuts import redirect

# def logout_view(request):
#     # Supprimer les clés de session de l'utilisateur
#     del request.session['user']
#     # Rediriger vers la page d'accueil ou une autre page appropriée
#     return redirect('index')







# def recherche_voiture(request):
#     if request.method == 'GET':
#         date_debut = request.GET.get('date_debut')
#         date_fin = request.GET.get('date_fin')

#         # Convertir les valeurs de date en objets datetime appropriés
#         date_prise_entre_f = datetime.strptime(date_debut, '%m/%d/%Y').date()
#         date_rendu_entre_f = datetime.strptime(date_fin, '%m/%d/%Y').date()

#         date_prise_entre = date_prise_entre_f.strftime('%Y/%m/%d')
#         date_rendu_entre = date_rendu_entre_f.strftime('%Y/%m/%d')
#         with connection.cursor() as cursor:
#             # cursor.execute("SELECT * FROM site_reservation_voiture WHERE id NOT IN (SELECT id_voiture FROM reservation_voiture WHERE (%s < date_reservation AND %s < date_reservation) OR (%s > date_rendu AND %s > date_rendu))", [date_prise_entre, date_rendu_entre, date_prise_entre, date_rendu_entre])
#             cursor.execute("SELECT * FROM site_reservation_voiture WHERE id NOT IN (SELECT id_voiture FROM reservation_voiture WHERE (%s < date_rendu AND %s > date_reservation) OR (%s > date_rendu AND %s < date_reservation))", [date_prise_entre, date_prise_entre, date_rendu_entre, date_rendu_entre])
#             voitures = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
                                                                                                                                       
#         request.session['date_fin'] = date_fin
#         context = {"voitures": voitures}
#         template = loader.get_template("site_reservation/recherche_voiture.html")
#         return HttpResponse(template.render(context, request))
#     else :
#         None



# def detail_voiture(request, voiture_id):
#     date_debut = request.session.get('date_debut')
#     date_fin = request.session.get('date_fin')

#     with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM site_reservation_voiture WHERE site_reservation_voiture.id = %s", [voiture_id])
#         voitures = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
    
#     context = {"voitures": voitures}
#     request.session['date_debut'] = date_debut
#     request.session['date_fin'] = date_fin
#     request.session['voiture_id'] = voiture_id
#     template = loader.get_template("site_reservation/detail_voiture.html")
#     return HttpResponse(template.render(context, request))


# def reservationVoiture(request):
#     date_debut = request.session.get('date_debut')
#     date_fin = request.session.get('date_fin')
#     voiture_id = request.session.get('voiture_id')

#     form = ReservationForm()
#     context = {'form': form}
#     request.session['date_debut'] = date_debut
#     request.session['date_fin'] = date_fin
#     template = loader.get_template("site_reservation/reservationVoiture.html")
#     return HttpResponse(template.render(context, request))




# def confirmationVoiture(request):
#     date_debut = request.session.get('date_debut')
#     date_fin = request.session.get('date_fin')

#     date_debut = datetime.strptime(date_debut, '%m/%d/%Y').date()
#     date_fin = datetime.strptime(date_fin, '%m/%d/%Y').date()

#     date_debut = date_debut.strftime('%Y/%m/%d')
#     date_fin = date_fin.strftime('%Y/%m/%d')

#     user_id = request.session.get('user_id')
#     voiture_id = request.session.get('voiture_id')


#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             # Traitez les données de réservation de voiture ici
#             nom = form.cleaned_data['nom']
#             with connection.cursor() as cursor:
#                 cursor.execute("INSERT INTO reservation_voiture (id, utilisateur_id, date_reservation, date_rendu, id_voiture) VALUES (null, %s, %s, %s, %s)", [user_id ,date_debut ,date_fin, voiture_id])
#                 connection.commit()
#                 cursor.close()

#             # Effectuez les actions nécessaires avec les données de réservation

#             # Redirigez vers la page de confirmation après la réservation
#             context ={}
#             print(voiture_id)
#             return render(request, 'site_reservation/reservationVoiture.html', context)
            
#     else:
#         form = None

#     context = {'form': form}
#     return render(request, 'site_reservation/reservationVoiture.html', context)








# def mes_reservations(request):
#     user_id = request.session.get('user_id')
    
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM reservation_voiture WHERE utilisateur_id = %s", [user_id])
#         reservations = cursor.fetchall()
#         cursor.close()

#     context = {'reservations': reservations}
#     return render(request, 'site_reservation/mesreservation.html', context)








from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from .forms import ReservationForm
from .models import Hotel

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

def confirmationVoiture(request):
    date_debut = request.session.get('date_debut')
    date_fin = request.session.get('date_fin')
    print(date_debut, date_fin)

    date_debut = datetime.strptime(date_debut, '%Y/%m/%d').date()
    date_fin = datetime.strptime(date_fin, '%Y/%m/%d').date()

    date_debut = date_debut.strftime('%Y/%m/%d')
    date_fin = date_fin.strftime('%Y/%m/%d')

    user = request.session.get('user')
    user_id = user['id']
    voiture_id = request.session.get('voiture_id')

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO reservation_voiture (id, utilisateur_id, date_reservation, date_rendu, id_voiture) VALUES (null, %s, %s, %s, %s)", [user_id ,date_debut ,date_fin, voiture_id])
                connection.commit()
            
            context ={}
            print(voiture_id)
            return render(request, 'site_reservation/reservationVoiture.html', context)
            
    else:
        form = None

    context = {'form': form}
    return render(request, 'site_reservation/reservationVoiture.html', context)


def mesreservation(request):
    user = request.session.get('user')
    user_id = user['id']
    print(user_id)
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM reservation_voiture WHERE utilisateur_id = %s", [user_id])
        reservations = cursor.fetchall()

    context = {'reservations': reservations}
    return render(request, 'site_reservation/mesreservation.html', context)



































# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# # import mysql.connector
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages

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