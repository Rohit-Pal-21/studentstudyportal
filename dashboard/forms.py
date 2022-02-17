from dataclasses import field
from random import choices
from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields=['title','description']

class DateInput(forms.DateInput):
    input_type= 'date'

class HomeworkForm(forms.ModelForm):
    class Meta:
        model=Homework
        widgets={'due':DateInput()}
        fields=['subject','title','description','due','is_finished']


class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100,label="Enter Your search :")


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','is_finished']


class ConversionForm(forms.Form):
    _CHOICES= [('length','Length'),('mass','Mass')]
    measurement = forms.ChoiceField(choices=_CHOICES,widget=forms.RadioSelect)


class ConversionLengthForm(forms.Form):
    _CHOICES= [('yard','Yard'),('foot','Foot')]
    input = forms.CharField(required=False,label=False, widget=forms.TextInput(
        attrs={'type':'number','placeholder':'Enter the Number'}
    ))
    measure1=forms.CharField(
        label='',widget=forms.Select(choices=_CHOICES)
    )
    measure2=forms.CharField(
        label='',widget=forms.Select(choices=_CHOICES)
    )


class ConversionMassForm(forms.Form):
    _CHOICES= [('pound','Pound'),('kilogram','Kilogram')]
    input = forms.CharField(required=False,label=False, widget=forms.TextInput(
        attrs={'type':'number','placeholder':'Enter the Number'}
    ))
    measure1=forms.CharField(
        label='',widget=forms.Select(choices=_CHOICES)
    )
    measure2=forms.CharField(
        label='',widget=forms.Select(choices=_CHOICES)
    )


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','password1','password2']





