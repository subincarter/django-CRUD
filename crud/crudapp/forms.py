from django import forms


class details(forms.Form):
    name = forms.CharField(max_length=20)
    age = forms.IntegerField()
    department = forms.CharField(max_length=10)
    address = forms.CharField(max_length=50)