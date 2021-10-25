from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http import HttpResponse



# Create your views here.
def index(request):
    qstobj = Question.objects.all()
    context = {'qst' : qstobj}
    return render(request, 'poll/index.html', context)

def showchoices(request, question_id):
    qstobj = Question.objects.get(pk=question_id)
    context = {'choice': qstobj}
    return render(request, 'poll/vote.html', context)

def voted(request, question_id):
    if request.method == 'POST':
        qstobj = Question.objects.get(pk=question_id)
        try:
            choiceobj = get_object_or_404(Choice, pk=request.POST['choice'])
        except:
            return HttpResponse("Please Vote")
        else:
            choiceobj.votes += 1
            choiceobj.save()
            return render(request, 'poll/index.html', {'choice': choiceobj})
    return render(request, 'poll/index.html')
    
