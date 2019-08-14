# pages/views.py
from django.shortcuts import render
import random


def index(request): # 첫 번째 인자는 반드시 request => 사용자가 보내는 요청에 대한 정보
    # 요청이 들어오면 index.html 을 보여준다.
    # templates 폴더에서 해당하는 파일을 찾아 보여준다.
    return render(request, 'index.html')  # render 의 첫 인자도 request, template_name => 만들고자 하는 페이지 이름
                                          
def introduce(request):
    return render(request, 'introduce.html')


# Template Cariable Example
def dinner(request):
    menu = ['강남 더막창스', '노랑통닭', '차돌짬뽕']
    pick = random.choice(menu)
    context = {
        'pick': pick,
    }

    # Django template 으로 context 전달
    return render(request, 'dinner.html', context)  # context 를 dinner.html 에 전달
