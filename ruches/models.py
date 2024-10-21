from django.db import models
from django.utils import timezone

class Rucher(models.Model):
    nom = models.CharField(max_length=100)
    emplacement = models.CharField(max_length=200)
    date_creation = models.DateField(auto_now_add=False, default=timezone.now)

    def __str__(self):
        return self.nom

class Reine(models.Model):
    id_reine = models.CharField(primary_key=True, max_length=50, null=False, blank=True)
    rucher = models.ForeignKey(Rucher, on_delete=models.CASCADE, related_name='reine')
    age = models.IntegerField()

    STATUT_CHOICES =(
        ('Normale', 'Normale'),
        ('Infecter', 'Infecter'),
    )
    sante = models.CharField(choices=STATUT_CHOICES, max_length=100)
    date_remplacement = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.id_reine

class Ruche(models.Model):
    rucher = models.ForeignKey(Rucher, on_delete=models.CASCADE, related_name='ruches')
    id_reine = models.ForeignKey(Reine, on_delete=models.CASCADE, related_name='reine')
    nom = models.CharField(max_length=100)
    date_inspection = models.DateField(auto_now_add=False, null=True, blank=True)
    niveaux_miel = models.FloatField(help_text="Niveau de miel en kg")
    infestations = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'Ruche {self.nom} du rucher {self.rucher.nom}'

class Recolte(models.Model):
    ruche = models.ForeignKey(Ruche, on_delete=models.CASCADE, related_name='recoltes')
    date_recolte = models.DateField(auto_now_add=False, null=True, blank=True)
    quantite_miel = models.FloatField(help_text="Quantité de miel récolté en kg")

    def __str__(self):
        return f'{self.quantite_miel} kg de miel récolté le {self.date_recolte}'

class Notification(models.Model):
    rucher = models.ForeignKey(Rucher, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    date_notification = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification: {self.message}'


