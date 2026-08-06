from django import forms
from .models import Withdrawal


class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = [
            "account_number",
            "bank_name",
            "account_name",
            "amount",
        ]

        widgets = {
            "account_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Account Number",
                "maxlength": "10",
            }),
            "bank_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Bank Name",
            }),
            "amount": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Amount",
            }),
            
             "account_name": forms.TextInput(attrs={
                            "class": "form-control",
                            "placeholder": "Account Name",
                        }),
        }