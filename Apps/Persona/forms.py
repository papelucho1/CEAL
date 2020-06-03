from django import forms
import datetime 

class addPersona(forms.Form):
    id_persona = forms.CharField()
    nombre = forms.CharField()
    fecha = forms.DateField(widget=forms.SelectDateWidget() , initial = datetime.date.today())