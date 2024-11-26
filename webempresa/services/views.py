from django.shortcuts import render
from .models import Service

def services(request):
    services = Service.objects.all()
    print(services)
    for service in services:
        print(service.title)
    return render(request, "services/services.html", {'services':services})