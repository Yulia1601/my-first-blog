from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #Фрагмент post/<int:pk>/ определяет шаблон URL-адреса.
    # post/ значит, что после начала строки URL должен содержать слово post и косую черту /. Пока всё в порядке.
    # <int:pk> — эта часть посложнее. Она означает, что Django ожидает целочисленное значение и преобразует его в представление — переменную pk.
    # / — затем нам нужен еще один символ / перед тем, как адрес закончится.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]