from django import forms
from .models import *

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']
        widgets = {
            'email' : forms.TextInput(attrs = {'class': 'form-control','type':"email" ,'name':"email" ,'id':"email", 'placeholder':"Email"}),
            }
        
        

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        
        widgets = {
          'name' : forms.TextInput(attrs = {'class': 'form-control','type':"text" ,'name':"name",'placeholder':"Your Name"}),
          'email' : forms.TextInput(attrs = {'class': 'form-control','type':"email" ,'name':"email" ,'id':"email", 'placeholder':"Email"}),
          'subject' : forms.TextInput(attrs = {'class': 'form-control', 'placeholder':"Subject"}),
          'message' : forms.Textarea(attrs = {'class': 'form-control','type':"message" ,'name':"email" ,'id':"email", 'placeholder':"Your Message"}),
          }
        
        
        
class ContactFormar(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        
        widgets = {
          'name' : forms.TextInput(attrs = {'class': 'form-control','type':"text" ,'name':"name",'placeholder':"اسمك"}),
          'email' : forms.TextInput(attrs = {'class': 'form-control','type':"email" ,'name':"email" ,'id':"email", 'placeholder':"بريدك الإلكتروني"}),
          'subject' : forms.TextInput(attrs = {'class': 'form-control', 'placeholder':"عنوان الموضوع"}),
          'message' : forms.Textarea(attrs = {'class': 'form-control','type':"message" ,'name':"email" ,'id':"email", 'placeholder':"رسالتك"}),
          }        