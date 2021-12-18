from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    param = {'name':'anmol'}
    return render(request,'index.html',param)
def capitalise(request):
    s = request.POST.get('text','Nothing Entered')
    val = request.POST.get('capital','off')
    va = request.POST.get('counter', 'off')
    t = 'Not Asked'
    if(val == 'on'):
        s = s.upper()
    if(va=='on'):
        t = len(s)
    para = {'s':s,'name':'PABLA','t':t}
    return render(request, 'cap.html',para)