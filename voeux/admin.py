from django.contrib import admin
from .models import Ecole, Formation, Voeu

class EcoleAdmin(admin.ModelAdmin):
    list_display = ('nom',)  # Affiche le nom dans la liste
    search_fields = ('nom',) # Barre de recherche sur le nom

class FormationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ecole')           # Affiche le nom et l'école associée
    search_fields = ('nom',)                  # Recherche sur le nom de la formation
    list_filter = ('ecole',)                  # Filtre par école

class VoeuAdmin(admin.ModelAdmin):
    list_display = ('user', 'formation', 'date_depot', 'statut')  # Colonnes utiles
    search_fields = ('user__username', 'formation__nom')           # Recherche par utilisateur ou formation
    list_filter = ('statut', 'formation__ecole')                   # Filtres par statut et école

admin.site.register(Ecole, EcoleAdmin)
admin.site.register(Formation, FormationAdmin)
admin.site.register(Voeu, VoeuAdmin)
