from django import forms            
from django.contrib.auth.models import User   # fill in custom user info then save it 

class UserForm(forms.ModelForm):
    class Meta:
        model = User  
        fields = ('username', 'password')
