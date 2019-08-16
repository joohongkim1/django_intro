# pages/views.py
from django.shortcuts import render
from datetime import datetime
import random


def index(request): # 첫 번째 인자는 반드시 request => 사용자가 보내는 요청에 대한 정보
    # 요청이 들어오면 index.html 을 보여준다.
    # templates 폴더에서 해당하는 파일을 찾아 보여준다.
    return render(request, 'index.html')  # render 의 첫 인자도 request, template_name => 만들고자 하는 페이지 이름
                                          

def introduce(request):
    return render(request, 'introduce.html')


# Template Cariable Example
def dinner(request, name):
    menu = ['강남 더막창스', '노랑통닭', '차돌짬뽕']
    pick = random.choice(menu)
    context = {
        'pick': pick,
        'name': name,
    }

    # Django template 으로 context 전달
    return render(request, 'dinner.html', context)  # context 를 dinner.html 에 전달


def image(request):
    # image url 을 context 에 담아서 image.html 에 전달
    image_url = 'https://picsum.photos/id/815/500/500'
    context = {
        'image_url': image_url,
    }

    return render(request, 'image.html', context)


def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'greeting.html', context)


def times(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'result': num1 * num2,
    }
    return render(request, 'times.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }

    return render(request, 'template_language.html', context)


def isitbirthday(request):
#     my_birth = '1992-05-21'
#     context = {
#         'my_birth': my_birth,
#     }

    return render(request, 'isitbirthday.html')


def lotto(request):
    real_lottos = [21, 25, 30, 32, 40, 42]
    lottos = sorted(list(random.sample(range(1, 46), 6)))

    context = {
        'real_lottos': real_lottos,
        'lottos': lottos,
    }
    
    return render(request, 'lotto.html', context)


def search(request):  # search 부터 result 까지의 흐름을 파악할 것
    return render(request, 'search.html')


def result(request):   # 중요하니까 잘 이해할 것, 흐름 파악 
    query = request.GET.get('query')
    category = request.GET.get('category')
    context = {
        'query': query,
        'category': category,
    }
    return render(request, 'result.html', context)


def lotto_pick(request):
    return render(request, 'lotto_pick.html')


def lotto_result(request):
    pick_num = request.GET.get('pick_num')
    pick_num = list(map(int, pick_num.split()))
    result_num = [21, 25, 30, 32, 40, 42]

    pick_num.sort()
    context = {
        'pick_num': pick_num,
        'result_num': result_num,
    }

    return render(request, 'lotto_result.html', context)


def static_example(request):
    return render(request, 'static_example.html')
