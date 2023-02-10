from logging import PlaceHolder
from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User 
from django.utils.translation import gettext,gettext_lazy as _
from .models import Post,News,Technology,Science,Contact
from blog.models import Post,Science,Technology,News

# UserChangeForm
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    ref_no = forms.CharField(label='Reference No',widget=forms.TextInput(attrs={'class':'form-control','PlaceHolder':'AB-01-S-9119'}))
    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        
        }

# login form
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','category','desc']
        labels = {'title':'Title','desc':'Description','category':'Post Category'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
        'desc':forms.Textarea(attrs={'class':'form-control'}),
        'category':forms.Select(attrs = {'class':'form-control'}),
         }
#for content updating purpose
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title','desc']
        labels = {'title':'Title','desc':'Description'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
        'desc':forms.Textarea(attrs={'class':'form-control'}),
        # 'category':forms.Select(attrs = {'class':'form-control'}),
         }

class ScienceForm(forms.ModelForm):
    class Meta:
        model = Science
        fields = ['title','desc']
        labels = {'title':'Title','desc':'Description'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
        'desc':forms.Textarea(attrs={'class':'form-control'}),
        # 'category':forms.Select(attrs = {'class':'form-control'}),
         }

class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ['title','desc']
        labels = {'title':'Title','desc':'Description'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
        'desc':forms.Textarea(attrs={'class':'form-control'}),
        # 'category':forms.Select(attrs = {'class':'form-control'}),
         }
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact 
        fields = ['name','email','address','message']
        labels = {'name':'Name','address':'Address','email':'Email','message':'Message'}
        widgets = {
        'name':forms.TextInput(attrs= {'class':'form-control'}),
        'email':forms.TextInput(attrs= {'class':'form-control'}),
        'address':forms.TextInput(attrs= {'class':'form-control'}),
        'message':forms.Textarea(attrs= {'class':'form-control'}),
        }