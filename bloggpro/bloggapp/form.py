from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _
from .models import Post,Contact
from django.forms import ModelForm
from django.forms import Textarea

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','message']
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',}))
    message = forms.CharField( widget=forms.Textarea(attrs={'class':'form-control',}))

    

#class EmailForm(forms.Form):
#    #name= forms.CharField(max_length=500)
#    name = forms.CharField(max_length=500, label="Name", widget=forms.TextInput(attrs={'class':'form-control'}))
#    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
#    message = forms.CharField(label='Message',widget=forms.Textarea(
#                        attrs={'class':'form-control'}))

#    def __str__(self):
#        return self.name



class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        label = {'first_name' : 'First Name',
        'last_name' : 'Last Name',
        'email' : 'Email'}

    username = forms.CharField(widget=forms.TextInput(attrs={
                                                                'class': 'form-control',
                                                                }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
                                                                'class': 'form-control',
                                                                }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
                                                                'class': 'form-control',
                                                                }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                                                                'class': 'form-control mb-4',
                                                                }))


class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':'form-control'}))
    password=forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title','decs']
        labels = {'title': 'Title', 'decs': 'Decription'}
        
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    decs = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',}))


