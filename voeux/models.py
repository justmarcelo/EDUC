from django.db import models
from django.contrib.auth.models import User

class Ecole(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class Formation(models.Model):
    nom = models.CharField(max_length=100)
    ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ecole.nom} – {self.nom}"

class Voeu(models.Model):
    STATUT_CHOICES = [
        ('En attente', 'En attente'),
        ('Accepté', 'Accepté'),
        ('Refusé', 'Refusé'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    date_depot = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=50, choices=STATUT_CHOICES, default='En attente')
    class Meta:
        unique_together = ('user', 'formation')
    def __str__(self):
        return f"{self.formation} ({self.statut})"
