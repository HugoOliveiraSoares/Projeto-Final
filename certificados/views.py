from django.shortcuts import render

def certificados(request):
    return render(request, 'certificados.html')