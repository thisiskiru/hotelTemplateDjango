from cProfile import label
from email.policy import default
from multiprocessing.dummy import Value
from tkinter.ttk import Progressbar
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from .models import User

from django import forms

class PasswordForm(PasswordChangeForm):
    
    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = User
        fields = ('password1','password2')
        widget = {
            'password1' : forms.PasswordInput(attrs={'class': 'form-control',
                                              'name' : 'password','required':True}),
            'password2' : forms.PasswordInput(attrs={'class': 'form-control',
                                              'name' : 'password2','required':True}),
           
             }

