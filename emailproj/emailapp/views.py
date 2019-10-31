from django.http import HttpResponse
from django.shortcuts import render
from .tasks import add
# Create your views here.
def index(request):
    a = add.delay(3,6)
    return HttpResponse(str(a))