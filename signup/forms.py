from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django import forms

from signup.models import Cridentials


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Lastname'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}))
    
    class Meta:
        model = Cridentials
        fields = ('first_name', 'last_name', 'email',)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs) 
        
        helper = self.helper = FormHelper()
        layout = helper.layout = Layout()
        for field_name, field in self.fields.items():
            layout.append(Field(field_name, placeholder=field.label))
        helper.form_show_labels = False

        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text = ""

class SignUpFormChangeForm(UserChangeForm):

    class Meta:
        model = Cridentials
        fields = ('first_name', 'last_name', 'email',)
