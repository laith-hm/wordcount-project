from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    enterdtext =  request.GET['enterdtext']
    enterlist = enterdtext.split()
    enterdict ={}
    for word in enterlist:
        if word in enterdict:
            enterdict[word] += 1
        else:
            enterdict[word]=1
    sorteddict = sorted(enterdict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'enterdtext':enterdtext,'ourcount':len(enterlist),'sorteddict':sorteddict})
def about(request):
    return render(request, 'about.html')
