from django import forms
from .models import User
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    # captcha = CaptchaField()
    email = forms.EmailField(label="ایمیل", widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="رمز عبور", widget=forms.PasswordInput(attrs={"class": "from-control"}))


class SpecialUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',
                  'password',
                  'first_name',
                  'last_name',
                  'phone_number',
                  'position',
                  'activity_field',
                  'company_name',
                  'description',)
        labels = {
            'email': 'ایمیل',
            'password': 'PIN#',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'phone_number': 'تلفن',
            'position': 'سمت',
            'activity_field': 'زمینه فعالیت',
            'company_name': 'نام شرکت',
            'description': 'نوضیحات',
        }


class AdminUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',
                  'password',
                  'first_name',
                  'last_name')
        labels = {
            'email': 'ایمیل',
            'password': 'PIN#',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
        }
