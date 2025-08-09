from django.urls import path
from . import views  # Импорт views из текущей папки

urlpatterns = [
    path('', views.index, name='index'),  # Если у тебя есть функция index в views.py
]