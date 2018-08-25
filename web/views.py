from django.shortcuts import get_object_or_404,render,redirect,HttpResponse
from .models import Change_type,Change_content,User
from django import forms
from django.http import HttpResponseRedirect
from django.contrib import auth
import random
def index(request):
    return render(request,'web/home.html')
def Xy_change(request):

    is_login = request.session.get('IS_LOGIN',False)
    if is_login:
      return render(request,'web/xychange.html')
    else:
        return render(request,'web/login.html')
def changement(request):
    typename = request.POST.get('type')
    if typename is not None:
        tp = Change_type.objects.get(Type_name=typename)
        rand = tp.change_content_set.order_by('?')[0]
        return render(request, 'web/xychange.html', {'rand': rand.Change_text})
    else:
        return HttpResponse('you are dick')
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = User.objects.filter(username__exact= username,password__exact= password)
    if user :
        request.session['IS_LOGIN'] = True
        return redirect('web:change')
    else:
        return render(request,'web/login.html')
def logout(request):
    request.session.clear()
    return redirect('web:login')

def Hsy(request):
    name = request.POST.get('word')
    if name is not None:
        name_list = random.sample(name,len(name))
        reword =""
        for i in range(len(name_list)):
             reword = reword + name_list[i]
        return render(request,'web/hsy.html',{'reword':reword,'word':name})
    else:
        return render(request,'web/hsy.html')







