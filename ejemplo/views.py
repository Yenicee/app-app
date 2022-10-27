from django.shortcuts import render

def index(request):
    return render(request, "ejemplo/saludar.html",{"nombre":"Yenice"})

def index_uno(request):
    return render(request, "ejemplo/saludar.html",
    {"notas": [1,2,3,4,5,6,7,8,9]} 
    )

