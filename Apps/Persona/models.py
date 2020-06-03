from django.db import models

# Create your models here.


class Persona(models.Model):
    id_persona = models.CharField(max_length=11,primary_key=True)
    nombre = models.CharField(max_length=50) 
    fecha = models.DateField()



