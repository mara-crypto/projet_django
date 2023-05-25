from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'), 
        path("about", views.about, name='about'),
        path("contact", views.contact, name='contact'),
        path("voiture", views.voiture, name='voiture'),
        path("chambre", views.chambre, name='chambre'),
        path("restaurant", views.restaurant, name='restaurant'),
        path("search_results", views.search_results, name='search_results'),
        path("search_chambre", views.search_chambre, name='search_chambre'),
        path("connection", views.connection, name='connection')
    ] 