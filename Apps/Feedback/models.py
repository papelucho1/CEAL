from django.db import models

from Apps.Persona.models import Persona


# Create your models here.



class Feedback(models.Model):
    id_feedback = models.AutoField(primary_key=True)
    fecha = models.DateField()
    total_efectividad = models.IntegerField()
    total_estilos = models.IntegerField()
    efectividad_del_estilo = models.IntegerField()
    id_persona= models.ForeignKey(Persona, null = True, blank=True, on_delete = models.CASCADE)