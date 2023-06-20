from django.shortcuts import render,HttpResponseRedirect
from .forms import Student
from .models import Data
from django.views.generic.base import TemplateView,RedirectView
from django.views import View


class Getallview(TemplateView):
    def get(self,request,**kwargs):
        fm = Student()
        form = Data.objects.all() 
        return render(request,'enroll/home.html',{'forms':fm,'form':form})
    
    def post(self,request,**kwargs):
        fm = Student(request.POST)
        if fm.is_valid():
            fm.save()
            fm = Student()
            return render(request,'enroll/home.html',{'forms':fm})

class Deletedata(RedirectView):
    url = '/'
    def get(self,request,id, **kwargs):
        c = id
        print('delete data')
        Data.objects.get(pk=c).delete()
        return HttpResponseRedirect('/')
        
class Update(View):
    def get(self,request,id,**kwargs):
        pi = Data.objects.get(pk=id)
        fm = Student(instance=pi)
        return render(request,'enroll/update.html',{'forms':fm})

    def post(self,request,id,**kwargs):
        pi = Data.objects.get(pk=id)
        fm = Student(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return render(request,'enroll/update.html',{'forms':fm})
    