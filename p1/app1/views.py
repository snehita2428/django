from django.http import HttpResponse
from django.shortcuts import render
import operator
def myhome(requests):
   return render(requests,'app1/home.html',{'username':'snehi'})
def aboutus(requests):
   return render(requests,'app1/about.html',{'userid':'snehiid'})
