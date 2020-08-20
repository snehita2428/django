from django.shortcuts import render
from django.http import HttpResponse
import operator
def home(requests):
        return render(requests,'vremove/home.html')
def count(requests):
        x=['a','e','i','o','u']
        count=0
        mytext=requests.GET['fulltext']
        for i in mytext:
            if i in x:
                count+=1
        l=list(mytext)
        for i in l:
            if i in x:
                l.remove(i)
        mytext="".join(l)                                                
        return render(requests,'vremove/count.html',{'wc':count,'ytext':mytext})
# Create your views here.
