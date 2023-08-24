from django.urls import path, include
from WebSims import views
from WebSims.views import saludo



urlpatterns = [
    path('saludo/', saludo)
]

