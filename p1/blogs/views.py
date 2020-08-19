from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import operator

def drinks(requests):
    return HttpResponse('Drink 3 L water everyday will keep you hydrated')
def foods(requests):
    return HttpResponse('Dont eat market food - it is high in Salt')
