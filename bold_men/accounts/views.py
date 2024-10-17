from django.contrib.auth import logout
from django.contrib.auth.views import login_required
from accounts.forms import (
        ClientRegisterForm,
        IndividualRegisterForm,
        EmployeeRegisterForm,
        UserUpdateForm,
        ProfileUpdateForm,
        )
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.contrib import messages

from fabrics.models import Fabric
from .forms import CustomLoginForm
from django.contrib.auth.views import LoginView



class HomePage(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        featured_fabrics = Fabric.objects.all()[:3]
        context['featured_fabrics'] = featured_fabrics
        return context




def user_type_page(request):
    return render(request, "accounts/user_type.html")

def register_client(request):
    if request.method == "POST":
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('accounts:login')
    else:
        form = ClientRegisterForm()
    context = {'form': form}
    return render(request, "accounts/register_client.html", context)

def register_individual(request):
    if request.method == "POST":
        form = IndividualRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('accounts:login')
    else:
        form = IndividualRegisterForm()
    context = {'form': form}
    return render(request, "accounts/register_individual.html", context)

def register_employee(request):
    if request.method == "POST":
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('accounts:login')
    else:
        form = EmployeeRegisterForm()
    context = {'form': form}
    return render(request, "accounts/register_employee.html", context)


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = CustomLoginForm


@login_required
def user_logout(request):
    logout(request)
    return render(request, "accounts/logout.html")
    
@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('accounts:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
            'u_form': u_form,
            'p_form': p_form
            }
    return render(request, "accounts/profile.html", context)
    


