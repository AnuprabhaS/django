from django import forms

class EmpForm(forms.Form):
    ename=forms.CharField(label='Employeename',max_length=150)
    desig = forms.CharField(label='designation', max_length=150)
    sal=forms.IntegerField()
