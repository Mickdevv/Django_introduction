from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200, required=True)
    check = forms.BooleanField(label="Available", required=False)
    age = forms.IntegerField(label="Age")

class CreateNewitem(forms.Form):
    name = forms.CharField(label="Name", required=False)
    age = forms.IntegerField(label="Age", max_value=150)