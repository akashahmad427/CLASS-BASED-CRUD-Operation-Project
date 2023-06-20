from django import forms
from .models import Data
class Student(forms.ModelForm):
    class Meta:
        model = Data
        fields = ('id','name','email','password')
        widgets = {'password':forms.PasswordInput(render_value=True)}
        error_messages = {'name':{'required':'Enter your name please'},
                          'email':{'required':'Enter your email please'},
                          'password':{'required':'Enter your password please'}}
        
    