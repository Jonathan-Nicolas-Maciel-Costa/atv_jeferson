from .views import RegisterAPIView,\
                   LoginAPIView
from django.urls import path, include

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name="Register"),
    path('login', LoginAPIView.as_view(), name='Login')
]
