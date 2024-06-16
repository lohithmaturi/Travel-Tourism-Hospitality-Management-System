from django import forms


from .models import Customer, LoginInfo, Admin


class Customer(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
class LoginInfo(forms.ModelForm):
    class Meta:
        model=LoginInfo
        fields="__all__"
# class Book(forms.ModelForm):
#     class Meta:
#         model=Book
#         fields="__all__"
class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"
        widgets = {"password":forms.PasswordInput()}
# class Contact(forms.ModelForm):
#     class Meta:
#         model=Contact
#         fields="__all__"

