from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import ValidationError
from apps.customer.models import Profile

class MyRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', required=True, widget = forms.PasswordInput(render_value=False, attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', required=True, widget = forms.PasswordInput(render_value=False, attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise ValidationError("The Email already exists")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError("The Username already exists")

    def clean_repassword(self):
        password = self.cleaned_data['password']
        repassword = self.cleaned_data['repassword']
        if password != repassword:
            raise ValidationError("The Password didn't match. Please try again")
        return repassword

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','discount']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'business_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address_line1': forms.TextInput(attrs={'class': 'form-control'}),
            'address_line2': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'postcode': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
        }


