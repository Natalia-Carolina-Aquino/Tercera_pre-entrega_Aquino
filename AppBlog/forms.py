from django import forms

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class KnitsForm(forms.Form):
    name = forms.CharField()
    knit_type = forms.CharField()
    material = forms.CharField()

class YarnsForm(forms.Form):
    name = forms.CharField()
    brand = forms.CharField()
    color = forms.CharField()
    width = forms.IntegerField()
    material = forms.CharField()

class AccesoriesForm(forms.Form):
    name = forms.CharField()
    knit_type = forms.CharField()
    material = forms.CharField()
    width = forms. CharField()
    length = forms.CharField()
    price = forms.CharField()

class SearchKnitsForm(forms.Form):
    name= forms.CharField()