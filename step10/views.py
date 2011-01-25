# Create your views here.
from django.shortcuts import render_to_response
from step10.models import *
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
import settings
from django.template.context import RequestContext


def mainView(request):
    questions = Question.objects.all()
    logouturl = settings.LOGOUT_URL
    loginurl = settings.LOGIN_URL
    return render_to_response('main.html', locals(),context_instance=RequestContext(request))

def showMyResults(request):
    logouturl = settings.LOGOUT_URL
    loginurl = settings.LOGIN_URL
    graph_values = []
    graph_lebels = []
    answer_sets = AnswerSet.objects.filter(author = request.user)
    for answer_set in answer_sets:
        graph_lebels.append(answer_set.date)
        graph_values.append(answer_set.count)
    return render_to_response('myresults.html', locals(),context_instance=RequestContext(request))


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", {
        'form': form,
    })

def saveResults(request):
    elements_to_save = []
    answer_set = AnswerSet()
    answer_set.author = request.user
    answer_set.save()
    for param in request.POST.items():
        field_id = param[0]
        field_value = param[1]
        if field_id.startswith('ID_') and field_value != None and len(field_value)>0:
            id = field_id.split('_')[1]
            answer = SavedAnswer()
            answer.answer_set = answer_set
            answer.question = Question.objects.get(id=id)
            answer.answer = field_value
            answer.save()  # should be outside for speed-up..
            elements_to_save.append(answer)

    answer_set.count = len(elements_to_save)
    answer_set.save()


    return HttpResponseRedirect("/")


def about(request):
    return render_to_response('about.html', locals(),context_instance=RequestContext(request))
