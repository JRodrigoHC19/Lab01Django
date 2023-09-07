from django.shortcuts import render

# Create your views here.
from .models import Operacion

def matematicas(request ,operador ,p1, p2):
    return render(request, 'operaciones.html', {'op':operador, 'p1' : p1, 'p2' : p2}
)
