from django import forms
from .import models
from django.contrib.auth.models import User 


class defaultform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        widgets={
            'password':forms.PasswordInput()
        }

class DateInput(forms.DateInput):
    input_type: str='date'

class  regform(forms.ModelForm):
    class Meta:
        model=models.regmodel
        fields=['contact','date']
        widgets={
            'date': DateInput()
            
        }
        



