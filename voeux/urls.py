from django.urls import path
from . import views

app_name = 'voeux'
urlpatterns = [
    path('depot/', views.depot_voeux, name='depot_voeux'),
    path('suivi/', views.suivi_voeux, name='suivi_voeux'),
]
