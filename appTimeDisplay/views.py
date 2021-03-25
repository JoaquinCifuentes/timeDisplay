from django.shortcuts import render, HttpResponse
from time import strftime, gmtime

def index(request):
    hora = strftime("%H:%M:%S")
    fecha =strftime("%d %B %Y")
    context = {
          "horaTemplate": hora,
          "fechaTemplate": fecha
        
    }
   # return render(request, "index.html",  context)
    return render(request, "index.html", context)