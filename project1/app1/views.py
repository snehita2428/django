from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(requests):
   return render(requests,'appp1/home.html')
def aboutus(requests):
   return render(requests,'app1/about.html')
