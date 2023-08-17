from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm (UserCreationForm):
    first_name=forms.CharField(max_length=50, required=False, help_text="Optional")
    last_name=forms.CharField(max_length=50, required=False,help_text="Optional")
    email=forms.EmailField(max_length=100, help_text="Required")
class Meta:
    """
    Configuration class for the SignUpForm class.
    Specifies the model to be used and the fields to include in the form.
    """
    model = User
    fields = ('first_name', 'last_name', 'username', 'email')
        # come later to ensure that all the details can be captured 


        



    