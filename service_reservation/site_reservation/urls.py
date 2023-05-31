


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('voiture/', views.voiture, name='voiture'),
    path('chambre/', views.chambre, name='chambre'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('connection/', views.connection, name='connection'),
    path('resultat/', views.resultat_view, name='resultat'),
    path('detail/', views.detail, name='detail')
]
