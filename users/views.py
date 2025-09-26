from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import InscriptionForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Inscription réussie !")
            return redirect('home')
    else:
        form = InscriptionForm()
    return render(request, 'users/inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Connexion réussie !")
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/connexion.html', {'form': form})

from django.contrib.auth.decorators import login_required
@login_required
def deconnexion(request):
    logout(request)
    messages.info(request, "Déconnexion réussie.")
    return redirect('home')
