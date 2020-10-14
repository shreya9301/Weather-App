from django.forms import ModelForm, TextInput
from django import forms

class Myform(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input is-rounded','placeholder':'Enter City name'})) 
