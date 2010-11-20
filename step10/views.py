# Create your views here.
from django.shortcuts import render_to_response
from step10.models import *



def mainView(request):
    user = request.user
    
    loginurl = '/login/'
    logouturl = '/logout/'
    questions = Question.objects.all()
    return render_to_response('main.html', locals())

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
