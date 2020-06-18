from .models import Alumni
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from phonenumber_field.formfields import PhoneNumberField


class UserRegisterForm(ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    class Meta:
        image = forms.ImageField()
        model = Alumni
        labels = {"current_job":
                 "Current Job and Location"}
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name',
                  'graduation_year', 'contact_number', 'current_job',
                  'linkedin_url', 'image']


class UserUpdateForm(ModelForm):
    class Meta:
        model = Alumni
        labels = {"current_job":
                 "Current Job and Location"}
        fields = ['first_name', 'last_name', 'graduation_year', 'contact_number',
                  'current_job', 'linkedin_url', 'image']
