from django.shortcuts import render

def sobre_mim(request):
    return render(request, 'sobre_mim.html')