from django import forms


class QRCodeForm(forms.Form):
    prefix = forms.CharField(max_length=100, required=False)
    suffix = forms.CharField(max_length=100, required=False)
    zeros = forms.CharField(required=False)
    amount = forms.CharField()
    logo = forms.ImageField(required=False)
