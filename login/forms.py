from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from signup.models import Cridentials

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    
    class Meta:
        model = Cridentials
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs) 
    
        helper = self.helper = FormHelper()
        layout = helper.layout = Layout()
        for field_name, field in self.fields.items():
            layout.append(Field(field_name, placeholder=field.label))
        helper.form_show_labels = False