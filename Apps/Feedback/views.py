from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from Apps.Feedback.models import Feedback 
from Apps.Persona.models import Persona
from Apps.Preguntas.models import Alternativa_seleccionada, Alternativa



# Create your views here.


def showFeedback(request,id_feedback):
    feedback_details = Feedback.objects.get(id_feedback = id_feedback)
    print ("feedback details -> ", feedback_details )
    id_person = feedback_details.id_persona_id
    print("id_persona -> ", id_person)
    person = Persona.objects.get(id_persona = id_person) 
    print ("person -> ", person)

    #contar los estilo 
    id_fdback = feedback_details.id_feedback
    getEstilos = Alternativa_seleccionada.objects.filter(id_feedback = id_fdback )

    count_estilo1 = 0
    count_estilo2 = 0
    count_estilo3 = 0
    count_estilo4 = 0

    count_efectividad1 = 0
    count_efectividad2 = 0
    count_efectividad3 = 0
    count_efectividad4 = 0

    for i in getEstilos:
        print("entra al for ")
        id_altern = i.id_alternativa_id
        print("id_atern : ", id_altern)
        altern = Alternativa.objects.get(id_alternativa = id_altern)
        print("altern: ", altern)
        #estilo = altern.estilo
        #print("estilo ", estilo)
        
        if altern.estilo == 1:
            count_estilo1 += 1
            count_efectividad1 +=  altern.efectividad     
        elif altern.estilo == 2:
            count_estilo2 += 1
            count_efectividad2 +=  altern.efectividad   
        elif altern.estilo == 3:
            count_estilo3 += 1
            count_efectividad3 +=  altern.efectividad   
        elif altern.estilo == 4:
            count_estilo4 += 1  
            count_efectividad4 +=  altern.efectividad    
      



    context = {
        'feedback': feedback_details,
        'person': person, 
        'count_estilo1': count_estilo1,   
        'count_estilo2': count_estilo2, 
        'count_estilo3': count_estilo3, 
        'count_estilo4': count_estilo4, 
        'count_efectividad1': count_efectividad1,   
        'count_efectividad2': count_efectividad2,  
        'count_efectividad3': count_efectividad3,  
        'count_efectividad4': count_efectividad4,         
        }

    return render(request, 'certificate.html',  context)   