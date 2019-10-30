from django import forms

class EmpForm(forms.Form):
    name=forms.CharField(label='name',max_length=150)
    address = forms.CharField(label='address', max_length=150)
    total=forms.IntegerField()
