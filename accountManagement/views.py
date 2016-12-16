from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, ChangeEmailForm, ChangePasswordForm


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            if user is not None:
                return HttpResponseRedirect('/accountManagement/home')
            else:
                form = LoginForm()
        else:
            HttpResponse("form is not valid")
    else:
        form = LoginForm()
    return render(request, 'accountManagement/login.html', {'form': form})


def home(request):
    if request.user.is_authenticated:
        return render(request, 'base.html')
    else:
        return HttpResponseRedirect("/accountManagement/")


# @require_http_methods(["POST", ])
# @login_required(redirect_field_name='my_redirect_field')
def change_password_view(request):
    if request.method == 'POST':
        password_form = ChangePasswordForm(request.POST)
        if password_form.is_valid():
            old_password = password_form.cleaned_data['oldPassword']
            new_password = password_form.cleaned_data['newPassword']
            new_password_confirmation = password_form.cleaned_data['newPasswordConfirmation']
            if (new_password == new_password_confirmation) and (request.user.check_password(old_password)):
                request.user.set_password(new_password)
                request.user.save()
                user = authenticate(username=request.user.username, password=new_password)
                login(request, user)
                return HttpResponseRedirect("/accountManagement/home")

            else:
                return HttpResponse("password change failed")
        else:
            HttpResponse("form is not valid")
    else:
        password_form = ChangePasswordForm()
    return render(request, 'accountManagement/changePassword.html', {'passwordForm': password_form})


def change_email_view(request):
    if request.method == 'POST':
        email_form = ChangeEmailForm(request.POST)
        if email_form.is_valid():
            new_email = email_form.cleaned_data['newEmail']
            request.user.email = new_email
            request.user.save()
            return HttpResponseRedirect("/accountManagement/home")
        else:
            return HttpResponse("form is not valid")
    else:
        email_form = ChangePasswordForm()
    return render(request, 'accountManagement/changeEmail.html', {'emailForm': email_form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/accountManagement/")
