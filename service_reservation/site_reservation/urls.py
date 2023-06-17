from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'), 
        path("about", views.about, name='about'),
        path("contact", views.contact, name='contact'),
        path("voiture", views.voiture, name='voiture'),
        path("chambre", views.chambre, name='chambre'),
        path("restaurant", views.restaurant, name='restaurant'),
        path("detailvoiture", views.detailvoiture, name='detailvoiture'),
        path("connecter", views.connecter, name='connecter'),
        path("reserve_resto", views.reserve_resto, name='reserve_resto')
        path("connecter", views.connecter, name='connecter'),
        path("reserve_resto", views.reserve_resto, name='reserve_resto')
    ] 