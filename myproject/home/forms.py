from django import forms            
from django.contrib.auth.models import User
from home.models import Bill, BillLine   # fill in custom user info then save it 

class UserForm(forms.ModelForm):
    class Meta:
        model = User  
        fields = ('username', 'password')

class BillForm(forms.ModelForm):
	class Meta:
		model = Bill


class BillLineForm(forms.ModelForm):
	class Meta:2
		model = BillLine
		exclude =('bill_main',)
