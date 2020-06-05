from django import forms

class login(forms.Form):
  username=forms.CharField(max_length=20)
  password=forms.CharField(widget=forms.PasswordInput())
  age=forms.IntegerField()
  image=forms.ImageField()
  name=forms.CharField(max_length=20)

class sinup(forms.Form):
  username=forms.CharField(max_length=20)
  password=forms.CharField(widget=forms.PasswordInput()) 

class chat_data_form(forms.Form):
   msg=forms.CharField(max_length=254)
   image=forms.ImageField()
