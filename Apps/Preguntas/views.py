from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse

from Apps.Preguntas.models import Pregunta, Alternativa, Alternativa_seleccionada

from Apps.Feedback.models import Feedback

# Create your views here.
from .models import * 
from Apps.Persona.models import Persona


#muestra pregunta por numero de pagina arriba
def index(request,num):
    question = Pregunta.objects.get(pk=num)
   #answer =  Pregunta.objects.get(pk=num).Alternativa_set.all() 
    answer =  Alternativa.objects.filter(id_pregunta = num)
   # answer = Alternativa.objects.get(id_pregunta = num)    
   # Article.objects.filter(reporter__first_name='John')   
    context = {               
        'questions': question,
        'answers' : answer
        }
    return  render (request,'base.html', context)

#muestra todas las preguntas
def showAllQuestions(request,id_person):
    question = Pregunta.objects.all()   
   
    answer =  Alternativa.objects.all()
    owner = Persona.objects.get(id_persona = id_person)
    #print (owner)
    feedback = Feedback.objects.get(id_persona = id_person)
   
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        post = request.POST

        sum_estilo = 0
        sum_efectividad = 0
        efectividadDelEstilo = 0

        for i in range(1,13):                 
            print ("post[i] : ", post[str(i)])
            alternativeSelected = int(post[str(i)])  #se selecciona la id de la alternativa
            #se obtienen los datos de la alternativa seleccionada    
            alternative = Alternativa.objects.get(id_alternativa = alternativeSelected )
            #suma de la efectividad y estilo 
            sum_estilo += alternative.estilo 
            sum_efectividad += alternative.efectividad

            #cargar datos en tabla alternativa_seleccionada
            answer_text = Alternativa.objects.get(id_alternativa = alternativeSelected)
            newAlternativaSelected = Alternativa_seleccionada(id_alternativa_id = alternativeSelected, id_feedback_id = feedback.id_feedback, respuesta_text = answer_text.respuesta  )
            newAlternativaSelected.save()
             
        ###### END FOR

        #calculo de efectividad del estilo 
        efectividadDelEstilo = (sum_efectividad/sum_estilo) * 12
        
        
        #id_person = owner.id_persona
        #date_test = owner.fecha
        #se genera feedback segun el test ingresado
        
        #feedbackEdited = Feedback(instance = feedback, total_efectividad= sum_efectividad , total_estilos =  sum_estilo, efectividad_del_estilo = efectividadDelEstilo )
        #feedback = Feedback( total_efectividad= sum_efectividad , total_estilos =  sum_estilo, efectividad_del_estilo = efectividadDelEstilo, id_persona_id = id_person)
        feedback.total_efectividad = sum_efectividad
        feedback.total_estilos = sum_estilo
        feedback.efectividad_del_estilo = efectividadDelEstilo
        feedback.save()
        
        #id_feedback = newFeedback.id_feedback

            
        ###end for            
          

        #return HttpResponse ("hola q hace")
        return HttpResponseRedirect(reverse('feedback', args=(feedback.id_feedback,)))
        
        # check whether it's valid:

        #enviar a Feedback 
        #return HttpResponseRedirect(reverse('questionary', args=(newPerson.id_persona,)  ))
        
          

    # if a GET (or any other method) we'll create a blank form
    else:
        context = {               
        'questions': question,
        'answers' : answer,
        'person': owner
        }
        return  render (request,'base.html', context)

        







    

#not sure about this one / this doesnt work 
def questions_detail_view(request,num):
    question = Pregunta.objects.get(pk = num)
    answer =  Pregunta.objects.get(pk = num).Alternativa__set.all() 
    context = {
        'questions' : question,
        'answers' : answer,
    }
    return render(request, 'preguntas_list.html', context)

    








