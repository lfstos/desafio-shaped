from django.db import models
from paciente.models import Paciente

# Create your models here.


class Exame(models.Model):
    profissional = models.CharField(max_length=50)
    dt_exame = models.DateField()
    peso = models.FloatField()
    altura = models.FloatField()
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)