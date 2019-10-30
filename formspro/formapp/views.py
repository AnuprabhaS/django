from django.shortcuts import render
from . forms import EmpForm
from .models import Student

# Create your views here.

def homepage(request):
    return render(request,'formapp/home.html')

def createEmp(request):
    if request.method=='GET':
        form=EmpForm()
        return render(request, 'formapp/registration.html',{'form':form})

    if request.method=='POST':
        form=EmpForm(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESS!")
            name=form.cleaned_data['name']
            adrs=form.cleaned_data['address']
            total=request.POST.get('total')
            # print("Salary:",salary)
            S=Student(name=name,address=adrs,total=total)
            S.save()
            # return render(request, 'formapp/registration.html', {'form': form})
            return disp(request)
def disp(request):
    data=Student.objects.all()
    return render(request, 'formapp/display.html', {'data': data})




