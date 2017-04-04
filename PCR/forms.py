from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(label='User Name',max_length=100)
    pwd = forms.CharField(widget=forms.PasswordInput,label='Password')


class AlertForm(forms.Form):
    sar_no = forms.CharField(label='Sar No',max_length=100)
    med = forms.CharField(label='Medications', max_length=100)

