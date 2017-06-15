from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question

def index(request): # ex: /polls/
    # latest_question_list: Aqui me vas a traer objetos del modelo Question, me los vas a organizar por pub_date y me traes 5 en total.
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context: Vas hacer una lista de latest_question_list y me lo vas almacenar en context.
    context = {'latest_question_list': latest_question_list}
    # return: Renderiza la request en el archivo /templates/polls/index.html inyectandole todo lo que viene en context.
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # question: Obtiene el objeto Question, si no existe llevame a un error 404. El pk (primary key) es igual a question_id
    question = get_object_or_404(Question, pk=question_id)
    # return: Renderiza la request en el archivo /templates/polls/detail.html inyectandole todo lo que viene en {'question': question}. No se guarda en una variable debido a que solo hay 1 resultado (DRY).
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    # question: Obtiene el objeto Question, si no existe llevame a un error 404. El pk (primary key) es igual a question_id
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    return HttpResponse("You're voting on question %s." % question_id)