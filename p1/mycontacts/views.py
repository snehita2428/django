from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import operator

def names(requests):
    return HttpResponse('family,friends,unknown')
def numbers(requests):
    return HttpResponse('Indian number consists of 10 digits')


# Create your views here.
