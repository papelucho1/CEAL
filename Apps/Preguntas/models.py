from django.db import models

from Apps.Feedback.models import Feedback

# Create your models here.

class Pregunta(models.Model):
    id_pregunta = models.IntegerField(primary_key=True)
    encabezado = models.CharField(max_length=500)


    def __str__(self):
        return self.encabezado


class Alternativa(models.Model):
    id_alternativa = models.AutoField(primary_key=True)
    letter_alternative = models.CharField(max_length=1)
    respuesta = models.CharField(max_length=250)
    estilo = models.IntegerField()
    efectividad = models.IntegerField() 
    id_pregunta = models.ForeignKey(Pregunta, null = True, blank=True, on_delete = models.CASCADE)


    
class Alternativa_seleccionada(models.Model):
    id_alternativa_seleccionada = models.AutoField(primary_key=True)
    id_alternativa = models.ForeignKey(Alternativa, null = True, blank=True, on_delete = models.CASCADE)
    id_feedback = models.ForeignKey(Feedback, null = True, blank=True, on_delete = models.CASCADE)
    respuesta_text = models.CharField(max_length=250,null = True)