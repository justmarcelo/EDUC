from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('logout/', views.deconnexion, name='logout'),
]