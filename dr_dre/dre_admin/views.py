from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import  UserRegisterForm, UserProfileCreationForm
from .models import Profile
from datetime import datetime

def NewName(newname):
    i = 1
    New_User = newname
    AllUsers = User.objects.values_list('username', flat=True).all()
    for oneuser in AllUsers:
        while New_User == oneuser:
            New_User = newname + str(i)
            i += 1
    return New_User



def register(request):
    profiles = Profile.objects.all().order_by('user__id')
    if request.method == 'POST':
        form1 = UserRegisterForm(request.POST)
        form2 = UserProfileCreationForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            firstname = form1.cleaned_data.get('first_name')
            lastname = form1.cleaned_data.get('last_name')
            username = str(firstname).lower()[0] + str(lastname).lower()
            newname = NewName(username)
            password = newname + '@123'
            email = form1.cleaned_data.get('email')
            isactive = form1.cleaned_data.get('is_active')
            usr = User(first_name = firstname, last_name = lastname,
                        username = newname,
                        email = email, is_active = isactive, date_joined = datetime.now())
            usr.set_password(password)
            usr.save()
            pro = Profile(user = usr, role = form2.cleaned_data.get('role'))
            pro.save()
            messages.success(request, f'Your account has been created, you can now log in :)')
    else:
        form1 = UserRegisterForm()
        form2 = UserProfileCreationForm()
    context = {
            'profiles': profiles,
            'form1': form1,
            'form2': form2
        }
    return render(request, 'dre_admin/register_user.html', context)

@login_required
def profile(request):
    """if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been successfully updated :)')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
        

    context = {'u_form': u_form,'p_form': p_form}"""
    return render(request, 'dre_admin/profile.html')