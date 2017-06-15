from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Choice, Question

def index(request): # ex: /polls/
    # latest_question_list: Aqui me vas a traer objetos del modelo Question, me los vas a organizar por pub_date y me traes 5 en total.
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context: Vas hacer una lista de latest_question_list y me lo vas almacenar en context.
    context = {'latest_question_list': latest_question_list}
    # return: Renderiza la request en el archivo /templates/polls/index.html inyectandole todo lo que viene en context.
    return render(request, 'polls/index.html', context)

def detail(request, question_id): # ex: /polls/[0-9]/
    # question: Obtiene el objeto Question, si no existe llevame a un error 404. El pk (primary key) es igual a question_id
    question = get_object_or_404(Question, pk=question_id)
    # return: Renderiza la request en el archivo /templates/polls/detail.html inyectandole todo lo que viene en {'question': question}. No se guarda en una variable debido a que solo hay 1 resultado (DRY).
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id): # ex: /polls/[0-9]/vote
    # question: Obtiene el objeto Question, si no existe llevame a un error 404. El pk (primary key) es igual a question_id
    question = get_object_or_404(Question, pk=question_id)
    try:
        # selected_choice = Almacenamos en una variable lo que viene en POST desde el template, solo lo que viene de choice. (Repasar)
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except: Si hay un error de tipeo en el form que viene de detail.html va mostrar un error, igualmente si el objeto 'Choice' no existe.
    except(KeyError, Choice.DoesNotExist):
        # return: Si hay error como mencione arriba me vas a renderrizar el archivo polls/detail.html y vas a inyectar el siguiente objeto 'question' y  me vas a dar el mensaje de error "You didn't select a choice."
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # selected_choice.votes: Al seleccionar el radio en especifico, me le agregas 1 al contador.
        selected_choice.votes += 1
        # selected_choice.save: Guardas el cambio.
        selected_choice.save()
    # Nota de Django Docs: Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button.
    # return: Retornamos a los resultados con el question.id para saber cual es id por el que se esta votando, gracias a HttpResponseRedirect. ex: /polls/3/results/
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))