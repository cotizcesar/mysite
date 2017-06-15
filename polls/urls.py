from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/ - Cuando alguien venga a /polls/ los va a redirigir al archivo importado "from . import views" que es views.py y dentro hay una funcion que se llama index.
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/ - Cuando alguien solicite significa el question_id que esta retornando esa funcion llamada detail que esta en views.py es un numero. El name='detail' sirve para cuando las plantillas quieran una url se puedan usar con este tag {% url %}. Ex: <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/ - Esta es la url que esta usando la funcion results que esta en views.py usando el question_id.
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/ - Lo mismo que las anteriores funciones, esta dando el question_id para votar.
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]