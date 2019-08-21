from django.urls import path
from . import views  # from . <- 현재 경로에서부터 

urlpatterns = [
    path('push/', views.push),
    path('pull/', views.pull), 

    path('static_example/', views.static_example),
    path('lotto_pick/', views.lotto_pick),
    path('lotto_result/', views.lotto_result),
    path('result/', views.result),
    path('search/', views.search),

    path('lotto/', views.lotto),
    path('isitbirthday/', views.isitbirthday),
    path('template_language/', views.template_language),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('greeting/<str:name>/', views.greeting),
    path('image/', views.image),
    path('dinner/<str:name>/', views.dinner),
    path('introduce/', views.introduce),
    path('index/', views.index),  # view 에 있는 index 라고 하는 함수를 실행
    
]