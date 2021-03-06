from email.policy import default
from multiprocessing import AuthenticationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField
from .models import *
#-------------------------------------------------------------------------
#Clase Formulario Stalkers
class Formulario_Stalkers(forms.Form):

    Name= forms.CharField(max_length=30)
    Surname= forms.CharField(max_length=30)
    Faction= forms.CharField(max_length=30)
    DateOfBirth= forms.DateField()

#-------------------------------------------------------------------------
#Clase Formulario Facciones
class Formulario_Factions(forms.Form):

    name = forms.CharField(max_length=20) 
    founder = forms.CharField(max_length=30)
    leader = forms.CharField(max_length=30)
    allies = forms.CharField(max_length=100)
    neutral = forms.CharField(max_length=100)
    enemies = forms.CharField(max_length=100)

#-------------------------------------------------------------------------
#Clase Formulario Artefactos
class Formulario_Artifacts(forms.Form):

    name = forms.CharField(max_length=30)
    price = forms.CharField(max_length=30)
    advantage = forms.CharField(max_length=100)
    disavantage = forms.CharField(max_length=100)
    dateOfBirth = forms.DateField()

#-------------------------------------------------------------------------
class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput) #Cuando escriba aparecen los asteriscos
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()
        
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts ={k:"" for k in fields}

#-------------------------------------------------------------------------
class UserEditForm(UserCreationForm):

    
    email = forms.EmailField(label='Change E-Mail')
    password1= forms.CharField(label="Change Password", widget=forms.PasswordInput) #Cuando escriba aparecen los asteriscos
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()
        
    class Meta:
        model=User
        fields=['last_name', 'first_name','email', 'password1', 'password2']
        help_texts ={k:"" for k in fields}

#-------------------------------------------------------------------------
class AddAvatar(forms.Form):

    avatar=forms.ImageField(label="Avatar")


#------------------------------------------------------------------------

class Formulario_Posts(forms.Form):

    title= forms.CharField(max_length= 50)
    subtitle= forms.CharField(max_length= 50)
    body= RichTextField()
    author= forms.CharField(max_length=30)
    date = forms.DateField()


#------------------------------------------------------------------------




    

