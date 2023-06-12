


from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('voiture/', views.voiture, name='voiture'),
    path('chambre/', views.chambre, name='chambre'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('connection/', views.connection, name='connection'),
    path('resultat/', views.resultat_view, name='resultat'),
    path('detail/', views.detail, name='detail'),
    path('detail/<int:suite_id>', views.detail, name='detail'),
    path('reservation/detail/<int:suite_id>/', views.detail, name='detail'),
    path('signup/', views.signup, name='signup'),
    path('reservation/<int:user_id>/', views.reservation_view, name='reservation'),
    path('reservation/reservation/<int:suite_id>/', views.reservation_view, name='reservation'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('paiement/', views.paiement, name='paiement')

    

]

