from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import GuessNumbers
from .forms import PostForm


# Create your views here.
def index(req):
    lottos = GuessNumbers.objects.all()
    return render(req, 'lottoapp/index.html', {'lottos': lottos})

def post(req):
    if req.method == "POST":
        form = PostForm(req.POST) # POST를 통해 받은 데이터 추출

        if form.is_valid():
            lotto = form.save(commit=False) # DB 여기서 반영하지 않음
            lotto.generate()
            return redirect('index')
        else:
            return HttpResponse('ERROR!')

    elif req.method == "GET":
        form = PostForm()
        return render(req, 'lottoapp/postform.html', {'form': form})

def detail(req, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey)
    return render(req, 'lottoapp/detail.html', {'lotto': lotto})