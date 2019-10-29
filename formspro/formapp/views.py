from django.shortcuts import render
from . forms import EmpForm

# Create your views here.

def homepage(request):
    return render(request,'formapp/home.html')

def createEmp(request):
    if request.method=='GET':
        form=EmpForm()
        return render(request, 'formapp/registration.html',{'form':form})
