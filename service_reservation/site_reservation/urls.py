from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',                                    views.index,                  name='index'), 
    path("about",                               views.about,                  name='about'),
    path("contact",                             views.contact,                name='contact'),
    path("voiture",                             views.voiture,                name='voiture'),
    path("chambre",                             views.chambre,                name='chambre'),
    path("restaurant",                          views.restaurant,             name='restaurant'),
    path("recherche_voiture",                   views.recherche_voiture,      name='recherche_voiture'),
    path("detail_voiture/<int:voiture_id>/",    views.detail_voiture,         name='detail_voiture'),
    path("reservationVoiture",                  views.reservationVoiture,     name='reservationVoiture'),
    path("paiement",                            views.paiement,               name='paiement'),
    path("search_chambre",                      views.search_chambre,         name='search_chambre'),
    path('login',                               views.login,                  name='login'),
    path('signup',                              views.signup,                 name='signup'),
    path('logout',                              views.logout_view,            name='logout'),
    path('mesreservation',                      views.mesreservation,         name='mesreservation'),
    path('send_confirmation_email',                      views.send_confirmation_email,         name='send_confirmation_email')
    

]
