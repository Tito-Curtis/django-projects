
from django import forms
from .models import All_Users
from django.contrib.auth.hashers import make_password



class SignupForm(forms.ModelForm):
    firstName = forms.CharField(label="First Name",max_length=100)
    lastName = forms.CharField(label="Last Name",max_length=100)
    email    = forms.EmailField(label="Email" ,max_length=200)
    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    confirm_password  = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)

    class Meta:
        model = All_Users
        fields = ["firstName", "lastName", "email", "password","confirm_password"]
    
    def passwordClean(self):
        password = self.cleaned_data.get('password')         
        return make_password(password)   
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        email = cleaned_data.get('email')
 
        if All_Users.objects.filter(email=email).exists():
            #msg = 'Email has been used'
            #self.add_error('email', msg)
            raise forms.ValidationError('Email has been used')
        if password == confirm_password:
            specialCharacters = "!@#$%^&*()-_=+[{]}:|;'<,>.?/\\|`~"
            if len(password) < 6:
                raise forms.ValidationError('password too short')
                       
            if not(any(char.isalpha() for char in password) and any(char.isdigit() for char in password)):
                raise forms.ValidationError('password must contain at least a digit') 
            
            if not(any(char.isupper() for char in password)):
                raise forms.ValidationError('password must contain both digit and numbers')
                
            if not(any(char in specialCharacters for char in password )):
                raise forms.ValidationError('password must contain a special character')

        else:
            raise forms.ValidationError('Passwords do not match')

        
        return cleaned_data
    
    def save(self,commit=True):
        user = super().save(commit=False)
        user.password = self.passwordClean()
        user.firstName = self.cleaned_data.get('firstName').lower()
        user.lastName = self.cleaned_data.get('lastName').lower()
        user.email    = self.cleaned_data.get('email').lower()

        if commit:
            user.save()
        return user
    
class LoginForm(forms.Form):
    email = forms.EmailField(label="email", max_length=200)
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model = All_Users
        fields = ["email", "password"]
    



    
    

