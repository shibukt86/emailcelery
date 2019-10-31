from django.http import HttpResponse
from django.shortcuts import render
from .tasks import add,delaytime
# Create your views here.
def index(request):
    delaytime(30)
    return HttpResponse("direct")
def test2(request):
    delaytime.delay(30)
    return HttpResponse("celery")