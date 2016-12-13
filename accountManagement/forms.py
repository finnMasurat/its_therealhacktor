from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', max_length=20)


class ChangeEmailForm(forms.Form):
    newEmail = forms.CharField(label='New Email', max_length=50)


class ChangePasswordForm(forms.Form):
    oldPassword = forms.CharField(label='Old Password', max_length=20)
    newPassword = forms.CharField(label='New Password', max_length=20)
    newPasswordConfirmation = forms.CharField(label='Confirm new Password', max_length=20)

