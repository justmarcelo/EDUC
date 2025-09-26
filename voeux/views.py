from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VoeuForm
from .models import Voeu
from django.contrib import messages

@login_required
def depot_voeux(request):
    if request.method == 'POST':
        form = VoeuForm(request.POST)
        if form.is_valid():
            voeux = form.save(commit=False)
            voeux.user = request.user
            voeux.save()
            messages.success(request, "Vœu déposé avec succès !")
            return redirect('voeux:suivi_voeux')
    else:
        form = VoeuForm()
    return render(request, 'voeux/depot_voeux.html', {'form': form})

@login_required
def suivi_voeux(request):
    voeux = Voeu.objects.filter(user=request.user)
    return render(request, 'voeux/suivi_voeux.html', {'voeux': voeux})
