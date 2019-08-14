# Start Django



## 프로젝트폴더/settings.py

```python
*** 중요 ***
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```

## 출생신고 <- 꼭 해줘야 됨

```python
# Application definition

INSTALLED_APPS = [
    # Local apps <- 직접 생성한 앱, 가장 위쪽에 둠
    'pages',   # 생성한 어플리케이션명 
    
    # Third party apps <- 중간 위치에 둠
    
    # Django apps <- 기본적으로 등록되어 있는 앱, 항상 가장 아래쪽에 둠
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # 마지막 item에 , 작성 <= trailing comma
]
```



## 프로젝트폴더/urls.py

- 사용자가 들어올 수 있는 경로를 설정해주는 곳



## application 생성

```bash
$ python manage.py startapp pages <= pages 는 임의로 정한 이름
```

## admin.py  

-  관리자 페이지를 커스터마이징 하는 곳

## apps.py

- 해당 앱에 대한 정보가 입력되는 곳

## models.py

- 모델을 정의하는 곳
- 데이터베이스 관리, 저장할 데이터 정의

## test.py

- 작동하는지 안 하는지 `test code` 를 작성하는 곳, 쓸 일은 없다

## views.py  *****중요*****

- 일련의 작업들이 실제로 일어나는 함수를 정의하는 곳. 
- 사용자들에게 보여지는 페이지 담당, 특정 로직들 담당
- `url` 과 `view` 함수가 연동된다.
- 이 곳에 작성되는 함수를 `view` 함수라고 한다.



## Python File 3대장

- models.py , views.py, urls







