# <center> ✈ DJANGO-FLIGHT-PROJECT ✈ </center>

<img src="table.png" />

## <center> ************************************** </center>
# <center> 🚀 INITIAL SETUP </center>

```bash
# CREATING VIRTUAL ENVIRONMENT
# windows 👇
python -m venv env
# linux / Mac OS 👇
vitualenv env

# ACTIVATING ENVIRONMENT
# windows 👇
source env/Scripts/activate
# linux / Mac OS 👇
source env/bin/activate

# PACKAGE INSTALLATION
# if pip does not work try pip3 in linux/Mac OS
pip install djangorestframework
pip freeze > requirements.txt
django-admin startproject main .
# alternatively python -m pip install django
pip install python-decouple
django-admin --version
```

```bash
# 💨 If you already have a requirement.txt file, you can install the packages in the file
# 💨 by entering the following commands respectively in the terminal 👇
1-python -m venv env
2-source env/Scripts/activate
3-pip install -r requirements.txt 🚀
4-python.exe -m pip install --upgrade pip
5-python manage.py migrate
6-python manage.py createsuperuser
7-python manage.py runserver
```
## 🛑 Secure your project
## 🚩 .gitignore

✔ Add a ".gitignore" file at same level as env folder, and check that it includes ".env" and /env lines.

🔹 Do that before adding your files to staging area, else you will need extra work to unstage files to be able to ignore them.

🔹 [On this page](https://www.toptal.com/developers/gitignore) you can create "gitignore files" for your projects.

## 🚩 Python Decouple

💻 To use python decouple in this project, first install it 👇
```bash
pip install python-decouple
```

💻 Go to terminal to update "requirements.txt"  👇
```bash
pip freeze > requirements.txt
```

✔ Create a new file and name as ".env" at same level as env folder

✔ Copy your SECRET_KEY from settings.py into this .env file. Don't forget to remove quotation marks and blanks from SECRET_KEY

```
SECRET_KEY=-)=b-%-w+0_^slb(exmy*mfiaj&wz6_fb4m&s=az-zs!#1^ui7j
```

✔ Go to "settings.py", make amendments below 👇

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```
## 💻 INSTALLING DJANGO REST

💻 Go to terminal 👇

```bash
python manage.py makemigrations
python manage.py migrate
pip install djangorestframework
```

✔ Go to "settings.py" and add 'rest_framework' app to INSTALLED_APPS

## 💻 PostgreSQL Setup
💻 To get Python working with Postgres, you will need to install the “psycopg2” module👇

```bash
pip install psycopg2
```
💻 Go to terminal to update requirements.txt  👇
```bash
pip freeze > requirements.txt
```
✔ Go to settings.py and add '' app to INSTALLED_APPS

## 💻 Install Swagger
🔹 Explain a [sample API reference documentation](https://shopify.dev/api)

🔹 Swagger is an open source project launched by a startup in 2010. The goal is to implement a framework that will allow developers to document and design APIs, while maintaining synchronization with the code.

🔹 Developing an API requires orderly and understandable documentation.

🔹 To document and design APIs with Django rest framework we will use drf-yasg which generate real Swagger/Open-API 2.0 specifications from a Django Rest Framework API.

📜 You can find the documentation [here](https://drf-yasg.readthedocs.io/en/stable/readme.html).

### 💻 Go to terminal for installation 👇
```bash
pip install drf-yasg
```
💻 Go to terminal to update requirements.txt  👇
```bash
pip freeze > requirements.txt
```

✔ Go to "settings.py" and add 'drf_yasg' app to INSTALLED_APPS

## ✔ Here is the updated "urls.py" file for swagger. In swagger documentation, those patterns are not up-to-date 👇
```python
from django.contrib import admin
from django.urls import path
# Three modules for swagger:
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Flight Reservation API",
        default_version="v1",
        description="Flight Reservation API project provides flight and reservation info",
        terms_of_service="#",
        contact=openapi.Contact(
            email="rafe@clarusway.com"),  # Change e-mail on this line!
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path("admin/", admin.site.urls),
    # Url paths for swagger:
    path("swagger(<format>\.json|\.yaml)",
         schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0),
         name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc",
         cache_timeout=0), name="schemaredoc"),
]
```

## 💻 MIGRATE 👇
```bash
python manage.py migrate
```
## 🚀 RUNSERVER 👇
```bash
python manage.py runserver
```

### ✔ After running the server, go to [swagger page](http://127.0.0.1:8000/swagger/) and [redoc page](http://localhost:8000/redoc/) of your project!


## 💻 INSTALL DEBUG TOOLBAR 👇
🔹 The Django Debug Toolbar is a configurable set of panels that display various debug information about the current request/response and when clicked, display more details about the panel’s content.

📜 See the Django Debug Toolbar [documentation page](https://django-debug-toolbar.readthedocs.io/en/latest/).

💻 For Installation go to terminal 👇
```bash
pip install django-debug-toolbar
```
💻 Go to terminal to update "requirements.txt"  👇
```bash
pip freeze > requirements.txt
```

✔ Go to "settings.py" and add 'debug_toolbar' app to INSTALLED_APPS


## 🚩 Add django-debug-toolbar’s URLs to your project’s URLconf 👇
```python
from django.urls import include
urlpatterns = [
# ...
path('__debug__/', include('debug_toolbar.urls')),
]
```

## 🚩 Add the middleware to the top 👇
```python
MIDDLEWARE = [
"debug_toolbar.middleware.DebugToolbarMiddleware",
# ...
]
```

## 🚩 Add configuration of internal IPs to "settings.py" 👇
```python
INTERNAL_IPS = [
    "127.0.0.1",
]
```

## 🔴 SEPERATE DEV AND PROD SETTINGS:
🔹 When we start to deploy our Djang  application to the server or develop a Django application with the team, settings will be a serious problem.

🔹 There is no built-in universal way to configure Django settings without hardcoding them. But books, open-source and work projects provide a lot of recommendations and approaches on how to do it best. Let’s take a brief look at the most popular ones to examine their weaknesses and strengths.

### 👉 First Solution: Keeping local settings in "settings_local.py"
- This is the oldest method. I used it when I was configuring a Django project on a production server for the first time. I saw a lot of people use it back in the day, and I still see it now. The basic idea of this method is to extend all environment-specific settings in the settings_local.py file, which is ignored by VCS.

    - Pros: Secrets not in VCS.

    - Cons: settings_local.py is not in VCS, so you can lose some of your Django environment settings. The Django settings file is a Python code, so settings_local.py can have some non-obvious logic. You need to have settings_local.example (in VCS) to share the default configurations for developers.

### 👉 Second Solution: Separate settings file for each environment
🔹 This is an extension of the previous approach. It allows you to keep all configurations in VCS and to share default settings between developers.

🔹 In this case, you make a settings package with the following file structure:

![File_Structure](/file_structure.jpg?raw=true "Title")

## ✔ We prefer the second solution

## 🚩 In the "main" directory, create a new folder named "settings"

- Inside "settings" folder, create;
    - __init__.py which is the required file to create a python module.
    - base.py which will include common settings.
    - dev.py which will include developmend specific settings.
    - prod.py which will include production specific settings.

## 🚩 Copy all the staff inside "settings.py" to "base.py". And delete "settings.py"

## ✔ "base.py" file will be 👇
```python
"""
Django settings for main project.
Generated by 'django-admin startproject' using Django 4.1.
For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
from decouple import config
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #third party apps:
    'rest_framework',
    'drf_yasg',
    # 'debug_toolbar',

    #myApps:
]
MIDDLEWARE = [
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'main.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'main.wsgi.application'
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
""" DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
} """
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

## ✔ "dev.py" file will be 👇
```python
from .base import *
THIRD_PARTY_APPS = ["debug_toolbar"]
DEBUG = config("DEBUG")
INSTALLED_APPS += THIRD_PARTY_APPS
THIRD_PARTY_MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"]
MIDDLEWARE += THIRD_PARTY_MIDDLEWARE
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    "default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": BASE_DIR / "db.sqlite3",
    }
}
INTERNAL_IPS = [
"127.0.0.1",
]
```
## ✔ "prod.py" file will be 👇
```python
from .base import *
DATABASES = {
    "default": {
    "ENGINE": "django.db.backends.postgresql_psycopg2",
    "NAME": config("SQL_DATABASE"),
    "USER": config("SQL_USER"),
    "PASSWORD": config("SQL_PASSWORD"),
    "HOST": config("SQL_HOST"),
    "PORT": config("SQL_PORT"),
    "ATOMIC_REQUESTS": True,
    }
}
```

## ✔ "__init__.py" file will be 👇
```python
from .base import *
env_name = config("ENV_NAME")
if env_name == "prod":
    from .prod import *
elif env_name == "dev":
    from .dev import *
```

## ✔ Modify ".env" file with environment name, postgres and debug variables 👇
```python
ENV_NAME=dev
DEBUG=True
SQL_DATABASE=flight
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=localhost
SQL_PORT=5432
```
## 💻 MIGRATE THE LATEST CHANGES 👇
```bash
python manage.py migrate
```

## 🔴 LOGGING
🔹 Python programmers will often use print() in their code as a quick and convenient debugging tool. Using the [logging framework](https://docs.djangoproject.com/en/4.0/topics/logging/#logging) is only a little more effort than that, but it’s much more elegant and flexible. As well as being useful for debugging, logging can also provide you with more - and better structured - information about the state and health of your application.

🔹 Django uses and extends Python’s builtin logging module to perform system logging. This module is discussed in detail in Python’s own documentation; this section provides a quick overview.

🔹 A Python logging configuration consists of four parts 👇

- Loggers
- Handlers
- Filters
- Formatters

🔹 Python defines the following log levels 👇

- DEBUG: Low level system information for debugging purposes
- INFO: General system information
- WARNING: Information describing a minor problem that has occurred.
- ERROR: Information describing a major problem that has occurred.
- CRITICAL: Information describing a critical problem that has occurred.

✔ An example logging setting may be like 👇

```python
LOGGING = {
    "version": 1,
    # is set to True then all loggers from the default configuration will be disabled.
    "disable_existing_loggers": True,
    # Formatters describe the exact format of that text of a log record. 
    "formatters": {
        "standard": {
            "format": "[%(levelname)s] %(asctime)s %(name)s: %(message)s"
        },
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    # The handler is the engine that determines what happens to each message in a logger.
    # It describes a particular logging behavior, such as writing a message to the screen, 
    # to a file, or to a network socket.
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "ERROR",
            "stream": "ext://sys.stdout",
            },
        'file': {
            'class': 'logging.FileHandler',
            "formatter": "verbose",
            'filename': './debug.log',
            'level': 'INFO',
        },
    },
    # A logger is the entry point into the logging system.
    "loggers": {
        "django": {
            "handlers": ["console", 'file'],
            # log level describes the severity of the messages that the logger will handle. 
            "level": config("DJANGO_LOG_LEVEL", "INFO"),
            'propagate': True,
            # If False, this means that log messages written to django.request
            # will not be handled by the django logger.
        },
    },
}
```
## 📢 Django Settings: Best practices 👇
- Keep settings in environment variables.
- Write default values for production configuration (excluding secret keys and tokens).
- Don’t hardcode sensitive settings, and don’t put them in VCS.
- Split settings into groups: Django, third-party, project.
- Follow naming conventions for custom (project) settings.

# <center> ✏ This is the end of initial setup ✏ </center>

## <center> ****************************************************** </center>
# <center> 🚀 AUTHENTICATION </center>

## 🚩 ADDING AN APP

💻 Go to terminal 👇

```bash
python manage.py startapp users
```

✔ Go to "base.py" and add 'users' app to "INSTALLED_APPS"

## 💻 INSTALL [DJ-REST-AUTH](https://dj-rest-auth.readthedocs.io/en/latest/)
```bash
pip install dj-rest-auth
```
💻 Go to terminal to update "requirements.txt"  👇
```bash
pip freeze > requirements.txt
```
## 🚩 Add "dj_rest_auth" app to "INSTALLED_APPS" in your django "base.py" 👇

```python
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
```
## 🚩 Go to "main/urls.py" and add the path 👇
```python
path('users/', include('users.urls'))
```

## ✔ Create "urls.py" file under "users" App 👇
## 🚩 Go to "users/urls.py" and add 👇
```python
from django.urls import path, include

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]
```

## 💻 Migrate your database
```bash
python manage.py migrate
```

## ✔ Create "serializers.py" file under "users" App and add 👇
```python
from rest_framework import serializers, validators
# from django.contrib.auth.models import User
# from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"}

    )

    password1 = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password1'
        )

    def validate(self, data):
        if data['password'] != data['password1']:
            raise serializers.ValidationError(
                {"password": "Password didn't match..... "}
            )
        return data

    #! To create a user when the user is registered 👇
    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.pop('password1')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

```
## 🚩 Go to "views.py"
```python
from operator import ge
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
```

## 🚩 Go to "urls.py" and add the path 👇
```python
path('register/', RegisterView.as_view()),
```

## 🚩 Go to "base.py" and add 👇
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```

## 🚩 Create "signals.py" under "user" App and add 👇
```python
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```

## 🚩 Go to "apps.py" and add this under UsersConfig() 👇
```python
def ready(self) -> None:
    import users.signals
```

## 🚩 Go to "views.py" and customize RegisterView()👇
```python
from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    #! When user register 👉 "username", "email","first_name","last_name" and "token" will be returned. 👇
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.data
        if Token.objects.filter(user=user).exists():
            token = Token.objects.get(user=user)
            data['token'] = token.key
        else:
            data['error'] = 'User does not have token. Please login'
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
```

## 🚩 Override TokenSerializer() 👇
```python
from dj_rest_auth.serializers import TokenSerializer

#! We need to override the TokenSerializer to return all user data in a single request.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = {
            'username',
            'email'
        }

class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = {
            'key',
            'user'
        }
```

## 🚩 Go to "base.py" and add 👇
```python
REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'users.serializers.CustomTokenSerializer',
}
```
## <center> ****************************************************** </center>
# <center> 🚀 LOGIC STARTING </center>

- Flights:
    + Users:

        - views upcoming flights
    
    + Staff members:
        - views all flights with reservations
        - create flights

- Reservations :
    + Login_users:
        - create reservations:
        - views only their reservations

    + Staff_users:
        - create reservations
        - views all reservations
## 🚩 ADDING AN APP:

💻 Go to terminal 👇

```bash
python manage.py startapp flight
```

✔ Go to "base.py" and add 'users' app to "INSTALLED_APPS"

## 🚩 Go to "flight/models.py" and create Models 👇
```python
from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    flight_number = models.CharField(max_length=20)
    operating_airlines = models.CharField(max_length=20)
    departure_city = models.CharField(max_length=20)
    arrival_city = models.CharField(max_length=20)
    date_of_departure = models.DateField()
    etd = models.TimeField()

    def __str__(self):
        return f'{self.flight_number} - {self.departure_city} - {self.arrival_city}'

class Passenger(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    passenger = models.ManyToManyField(Passenger, related_name = 'reservations')
    #! 👆 It is possible to access the parent table that is related to via related_name. 👉 p.reservations.all()
    flight = models.ForeignKey(Flight, on_delete = models.CASCADE, related_name="reservation")
```

## 🚩 Register the models in "flight/admin.py" 👇
```python
from django.contrib import admin
from .models import Flight, Passenger, Reservation

admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Reservation)
```

## 💻 Go to terminal for migration 👇
```bash
python manage.py makemigrations
python manage.py migrate
```

## 🚩 Create "serializers.py" file under "flight" App 👇
```python
from rest_framework import serializers
from .models import Flight, Passenger, Reservation

class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = (
            "flight_number",
            "operating_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd"
        )
```

## 🚩 Time to add views in "flight/views.py" 👇
```python
from django.shortcuts import render
from .serializers import FlightSerializer
from rest_framework import viewsets
from .models import Flight, Passenger, Reservation

#! Thanks to the modelviewset, we can do all the operations 👇
#!  GET, POST, PUT, DELETE, PATCH
class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
```

## 🚩 Go to "main/urls.py" and add the path 👇
```python
path('flight/', include('flight.urls'))
```

## 🚩 Create "urls.py" file under "flight" App 👇
```python
from rest_framework import routers
from .views import FlightView

router = routers.DefaultRouter()
router.register('flights', FlightView)

urlpatterns = [

]

urlpatterns += router.urls
```

## 🚩 We will use "IsAdminUser" so that only the authorized user can create a flight. For that create "permissions.py" file under "flight" App 👇
```python
from rest_framework import permissions

class IsStafforReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
```

## 🚩 Go to "views.py" and add this permission 👇
```python
from .permissions import IsStafforReadOnly

class FlightView(viewsets.ModelViewSet):

    permission_classes = (IsStafforReadOnly,)
```

## 🚩 Go to "serializers.py" and add ReservationSerializer() 👇
```python
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            "id",
            "flight",  # GET
            "flight_id",  # POST
            "user",  # GET
            "user_id",  # POST
            "passenger"
        )
```

## 🚩 Go to "views.py" and add ReservationView() 👇
```python
from .serializers import ReservationSerializer
class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
```
## 🚩 Go to "flight/urls.py" and add the path 👇
```python
from .views import ReservationView
router.register('resv', ReservationView)
```

## 🚩 Go to "serializers.py" and add PassengerSerializer() 👇
```python
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"
```

## 🚩 In ReservationSerializer() add 👇
```python
passenger = PassengerSerializer(many = True, required=True)
flight = serializers.StringRelatedField()
flight_id = serializers.IntegerField(write_only=True)
#! write_only 👉 It will only appear when creating
user = serializers.StringRelatedField()
user_id = serializers.IntegerField(write_only=True, required=False)
```

## 🚩 We need to extract passenger information from the data, when the reservation is created. For that add to "serializers.py" 👇
```python
def create(self, validated_data):
        passenger_data = validated_data.pop('passenger')
        validated_data['user_id'] = self.context['request'].user.id
        # We updated the user information inside data 👆
        reservation = Reservation.objects.create(**validated_data)
        for passenger in passenger_data:
            pas = Passenger.objects.create(**passenger)
            reservation.passenger.add(pas)
        reservation.save()
        return reservation
```

## 🚩 All reservation information can only be seen by the staff user <i>(Users will only see their own reservation)</i>. For that override "get_queryset" method in "ReservationView()" in "views.py" 👇
```python
  #! Overriding "get_queryset" Method 👇
 def get_queryset(self):
        queryset = super().get_queryset() # 👉 Reservation.objects.all()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user = self.request.user)
```

## 🚩 Let the staff members see the reservation information of that flight for each flight. For this, we will add reservations to "FlightView()" by writing a separate serializer and say show it to staff 👇
```python
class StaffFlightSerializer(serializers.ModelSerializer):
    reservation = ReservationSerializer(many=True, read_only=True)
    class Meta:
        model = Flight
        fields = "__all__"
```

## 🚩 Go to "views.py" and override "get_serializer_class" in "FlightView()" 👇
```python
from .serializers import StaffFlightSerializer
def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.request.user.is_staff:
            return StaffFlightSerializer
        return serializer
```

## 🚩 We will override the "get_query_set" method in "FlightView()" so that normal users can't see past flights 👇
```python
from datetime import datetime, date
def get_queryset(self):
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        today = date.today()

        if self.request.user.is_staff:
            return super().get_queryset()
        else:
            queryset = Flight.objects.filter(date_of_departure__gt = today)
            if Flight.objects.filter(date_of_departure = today):
                today_qs = Flight.objects.filter(date_of_departure = today).filter(etd__gt=current_time)
            queryset = queryset.union(today_qs)
            return queryset
```
## 📢 Do not forget to check the endpoints you wrote in [Postman](https://www.postman.com/).
## <center>🥳 END OF TH  PROJECT 🥳</center>