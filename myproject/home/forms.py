from django import forms            
from django.contrib.auth.models import User
from home.models import Bill   # fill in custom user info then save it 

class UserForm(forms.ModelForm):
    class Meta:
        model = User  
        fields = ('username', 'password')

class BillForm(forms.ModelForm):
	class Meta:
		model = Bill
		fields = ('vendor', 'inv_num', 'terms', 'inv_date', 'due_date', 'gl_date', 'description', 'ammount')
