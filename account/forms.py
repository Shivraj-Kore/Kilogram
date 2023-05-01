from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200 , help_text="Requierd. Add a valid email please")

    class Meta :
        model = Account
        fields = ( 'email' , 'password1' , 'password2' , 'username' )

    def clean_email(self) :
        email = self.cleaned_data["email"].lower()
        try:
            account=Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already in use")
    
        
    def clean_username(self) :
        username = self.cleaned_data['username']
        try:
            account=Account.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"username {username} is already in use")
    
    
class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ("email" , "password")
        

    def clean (self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email , password= password):
                raise forms.ValidationError("Invalid login")