from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from django.urls import reverse

from Apps.Persona.models import Persona 
from Apps.Feedback.models import Feedback

from Apps.Persona.forms import addPersona


def beginTest(request):
   # print("paso 1")
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = addPersona(request.POST)
    
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['nombre']
            id_person = form.cleaned_data['id_persona']
            date = form.cleaned_data['fecha']
            
            try:
                testing = Persona.objects.get(id_persona = id_person)
                #newPerson = Persona(id_persona = id_person, nombre = name, fecha = date)

            except (KeyError, Persona.DoesNotExist):
                newPerson = Persona(id_persona = id_person, nombre = name, fecha = date)
                newPerson.save()

                # crear feedback para ingresar las preguntas
                newFeedback = Feedback(fecha = date, total_efectividad = 0, total_estilos = 0, efectividad_del_estilo= 0, id_persona_id = id_person)
                newFeedback.save()
                return HttpResponseRedirect(reverse('questionary', args=(newPerson.id_persona,)  ))
            else: 
                form = addPersona()        
                return render(request, 'index.html', {'formAddPerson': form})

            """       
            if Persona.objects.get(id_persona = id_person):
               form = addPersona()        
               return render(request, 'index.html', {'formAddPerson': form})   
            else:
                newPerson = Persona(id_persona = id_person, nombre = name, fecha = date)
                newPerson.save()
                # crear feedback para ingresar las preguntas
                newFeedback = Feedback(id_feedback= id_person,fecha = date, total_efectividad = 0, total_estilos = 0, efectividad_del_estilo= 0, id_persona_id = id_person)
                newFeedback.save()
                return HttpResponseRedirect(reverse('questionary', args=(newPerson.id_persona,)  ))
           
           """
           
           # id->431 name->JC              
            #usar esta funcion para moverc entre otras url 
            #return HttpResponseRedirect(reverse('questionary', args=(newPerson.id_persona,)))  
           
            #num = 1  
            #return render(request, 'base.html' )  
          

        else:
            return  HttpResponse("no es valido ") 
    # if a GET (or any other method) we'll create a blank form
    else:
        #mostrar en el template date = datetime.date.today()
        form = addPersona()
        
        return render(request, 'index.html', {'formAddPerson': form})   
    #return  HttpResponse("")
        

