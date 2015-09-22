from django.shortcuts import render

# Create your views here.

#!---Vista del inicio----
def inicio(request):
    return render(request,'inicio.html')

def registro(request):
    return render(request,'Registrarse.html')

def iniciar(request):
    return render(request,'Ini_Sesio.html')