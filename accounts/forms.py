from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


def styles():
    return '''w-full pl-xl pr-md py-sm bg-surface-container-low border border-outline-variant rounded-xl 
    focus:ring-2 focus:ring-primary focus:border-transparent transition-all outline-none font-body-md text-on-surface'
    '''

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "profile_photo",
            "first_name",
            "last_name",
            "username",
            "email",
            "phone",
            "password1",
            "password2",
        )

        widgets = {
            "first_name": forms.TextInput(attrs={
                "placeholder": "First Name"
            }),
            "last_name": forms.TextInput(attrs={
                "placeholder": "Last Name"
            }),
            "username": forms.TextInput(attrs={
                "placeholder": "Username"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Email Address"
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "Phone Number"
            }),
            'profile_photo': forms.ClearableFileInput(
                attrs={
            "class": "hidden",
            "accept": "image/*"
            })   
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        base_class = (
            "w-full bg-surface-container-lowest border "
            "border-outline-variant rounded-xl px-sm py-sm "
            "focus:ring-2 focus:ring-primary "
            "focus:border-primary")
        
        for name, field in self.fields.items():
            if name == "profile_photo":
                continue
            field.widget.attrs["class"] = base_class
        

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class':styles(),
            "placeholder": "Email Address"
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':styles(),
            "placeholder": "••••••••",
            'id':"password"
        })
    )

    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
        'class':'w-4 h-4 text-primary bg-surface-container border-outline-variant rounded focus:ring-primary',
    }
    )
    )