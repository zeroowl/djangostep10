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
    aset = AnswerSet()
    aset.author = request.user
    aset.save()
    for param in request.POST.items():
        if param[0].startswith('ID_'):
            id = param[0].split('_')[1]
            answer = SavedAnswer()
            answer.answer_set = aset
            answer.question = Question.objects.get(id=id)
            answer.answer = param[1]
            answer.save()

    aset.count = len(elements_to_save)
    aset.save()
    
    return render_to_response('main.html', locals())
