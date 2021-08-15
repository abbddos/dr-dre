from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import  UserRegisterForm, UserProfileCreationForm
from .models import Profile
from datetime import datetime
from django.contrib import messages

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
            try:
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
                messages.success(request, 'New user was successfully added :)')
                return redirect('register_user')
            except Exception as e:
                messages.error(request, str(e))
                return redirect('register_user')
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
def UpdateUser(request, uid):
    usr = User.objects.filter(id = uid).first()
    prf = Profile.objects.filter(user__id = uid).first()
    if request.method == 'POST':
        form1 = UserRegisterForm(request.POST)
        form2 = UserProfileCreationForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            try:
                usr.first_name = form1.cleaned_data.get("first_name")
                usr.last_name = form1.cleaned_data.get("last_name")
                usr.email = form1.cleaned_data.get("email")
                usr.is_active = form1.cleaned_data.get("is_active")
                usr.save()
                prf.role = form2.cleaned_data.get("role")
                prf.save()
                messages.success(request, 'User was successfully updated')
                return redirect('register_user') 
            except Exception as e:
                messages.error(request, str(e))
                return redirect('register_user')
    else:
        pass
    return redirect('register_user')

@login_required
def GetAllUsers(request):
    qry = Profile.objects.all()
    data = []
    for p in qry:
        profile = dict()
        profile["id"] = p.user.id
        profile["first_name"] = p.user.first_name
        profile["last_name"] = p.user.last_name
        profile["username"] = p.user.username
        profile["email"] = p.user.email
        profile["is_active"] = p.user.is_active
        profile["role"] = p.role
        data.append(profile)
    return JsonResponse({'data': data})

@login_required
def GetUserByID(response, uid):
    p = Profile.objects.filter(user__id = uid).first()
    profile = dict()
    profile["id"] = p.user.id
    profile["first_name"] = p.user.first_name
    profile["last_name"] = p.user.last_name
    profile["username"] = p.user.username
    profile["email"] = p.user.email
    profile["is_active"] = p.user.is_active
    profile["role"] = p.role
    return JsonResponse(profile)

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