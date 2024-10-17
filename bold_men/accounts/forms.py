from crispy_forms.layout import Field, Fieldset, Submit
from django import forms
from .models import Client, Individual, Employee, User, Profile
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper, Layout
from django.contrib.auth.forms import AuthenticationForm

# Adding crispy form design
# Custom admin page



class CustomLoginForm(AuthenticationForm):
    # add the necessary check there
    """
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    """
    ...


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'username']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ('user', 'date_of_birth',)

    ...
class ClientRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput)
    full_name = forms.CharField()
    bio = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Client
        fields = ['email', 'username', 'full_name', 'bio', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
                Fieldset(
                    'Personal Information',
                    Field('email', placeholder="adeleke@gmail.com"),
                    'password1',
                    'password2',
                    ),
                Fieldset(
                    'Additional Details',
                    'username',
                    'full_name',
                    'bio',
                    ),
                Submit('submit', 'Submit', css_class='btn btn-primary')
                )
        



class IndividualRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput)
    full_name = forms.CharField()
    bio = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Individual
        fields = ['email', 'username', 'full_name', 'bio', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
                Fieldset(
                    'Personal Information',
                    'email',
                    'password1',
                    'password2',
                    ),
                Fieldset(
                    'Additional Details',
                    'username',
                    'full_name',
                    'bio',
                    ),
                Submit('submit', 'Submit', css_class='btn btn-primary')
                )
        
class EmployeeRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={'placeholder': 'example@domain.com'}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Tell us about yourself...'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                'Account Information',
                'email',
                'username',
                'password1',
                'password2',
            ),
            Fieldset(
                'Personal Details',
                'full_name',
                'bio',
            ),
            Submit('submit', 'Register', css_class='btn btn-primary')
        )

    class Meta:
        model = Employee
        fields = ['email', 'username', 'full_name', 'bio', 'password1', 'password2']

