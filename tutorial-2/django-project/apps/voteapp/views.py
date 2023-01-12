from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question, Choice

# Create your views here.
def index(req):
    # '-' => desc
    latest_question_list = Question.objects.order_by('-pub_date')[:3]

    return render(req, 'voteapp/index.html', {'latest_question_list': latest_question_list})

def detail(req, question_id):
    try:
        q = Question.objects.get(pk = question_id)
        return render(req, 'voteapp/detail.html', {'question': q})

    except Question.DoesNotExist:
        raise Http404(f"Question {question_id} does not exist")

def results(req, question_id):
    q = get_object_or_404(Question, pk = question_id)
    return render(req, 'voteapp/results.html', {'question': q})

def vote(req, question_id):
    if req.method == "POST":
        try:
            q = Question.objects.get(pk = question_id)
            choice = q.choice_set.get(pk = req.POST['choice'])
            choice.votes += 1
            choice.save()
            return redirect('vote:results', question_id = q.id)

        except Question.DoesNotExist:
            raise Http404(f"Question {question_id} does not exist")
            
        except:
            raise Http404('올바른 선택을 하시오')
    else:
        raise Http404(f"올바르지 못한 접근")