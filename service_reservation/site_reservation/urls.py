


from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('', views.index, name='index'), 
        path("about", views.about, name='about'),
        path("contact", views.contact, name='contact'),
        path("voiture", views.voiture, name='voiture'),
        path("chambre", views.chambre, name='chambre'),
        path("restaurant", views.restaurant, name='restaurant'),
        path("search_results", views.search_results, name='search_results'),
        path("connecter", views.connecter, name='connecter'),
        path('login/', views.login, name='login'),
        path('resultat/', views.resultat_view, name='resultat'),
        path('detail/', views.detail, name='detail'),
        path('detail/<int:suite_id>', views.detail, name='detail'),
        path('reservation/detail/<int:suite_id>/', views.detail, name='detail'),
        path("reserve_resto", views.reserve_resto, name='reserve_resto'),
        path("reserve_resto", views.reserve_resto, name='reserve_resto'),
        path('signup/', views.signup, name='signup'),
        path('logout_view/', views.logout_view, name='logout_view'),
        # path('reservation/<int:user_id>/', views.reservation_view, name='reservation'),
        #path('reservation/reservation/<int:suite_id>/', views.reservation_view, name='reservation'),
        path("detailvoiture", views.detailvoiture, name='detailvoiture'),

        path('paiement/', views.paiement, name='paiement')
    ] 