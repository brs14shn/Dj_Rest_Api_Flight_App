from django.urls import path, include
from .views import RegisterView,logout

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path("register/", RegisterView.as_view()),
     path('logout/', logout, name='logout'),
]
