from django.shortcuts import render
from django.http import HttpResponse
from.models import Pytanie
from django.template import loader
# Create your views here.

def index(request):
    ostatnie_pytania=Pytanie.objects.order_by('-data_pub')[:5]
    template=loader.get_template('ankieta\index.html')
    context={'lista_pytan':ostatnie_pytania,}
    return HttpResponse(template.render(context,request))


def szczegoly(request, pytanie_id):
    return HttpResponse(f"Tutaj będą szczegóły - {pytanie_id}")


def wyniki(request, pytanie_id):
    return HttpResponse(f"Tutaj będą wyniki - {pytanie_id}")

def glosuj(request, pytanie_id):
    return HttpResponse(f"Głosujesz na pytanie - {pytanie_id}")