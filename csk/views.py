from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Captain(request):
    return HttpResponse('<h2>Ruturaj is the Captain of Chennai Super Kings</h2>')
