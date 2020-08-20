from django.shortcuts import render
from django.http import HttpResponse
import operator
def home(requests):
    return render(requests,'wc/home.html')
def count(requests):
    mytext=requests.GET['fulltext']
    wcount=mytext.split()
    n=len(wcount)
    mylist=[]
    s=set(wcount)
    for i in s:
        x=(i,len(i),wcount.count(i))
        mylist.append(x)
        
    return render(requests,'wc/count.html',{'wc':n,'ylist':mylist})
# Create your views here.
