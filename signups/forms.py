from django import forms


from .models import SignUP

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUP
