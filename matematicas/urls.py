from django.urls import path
from . import views

urlpatterns = [
    path('<str:operador>/<int:p1>/<int:p2>', views.matematicas, name='operaciones'),
]