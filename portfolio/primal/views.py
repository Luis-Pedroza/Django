from django.shortcuts import render

def primal(request):
    return render(request, 'primal.html')

def episodios(request):
    return render(request, 'episodios.html')

def extras(request):
    return render(request, 'extras.html')

def perfil(request):
    return render(request, 'perfil.html')

def personajes(request):
    return render(request, 'personajes.html')

def header(request):
    return render(request, 'header.html')