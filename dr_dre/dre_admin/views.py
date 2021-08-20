from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import  UserRegisterForm, UserProfileCreationForm, UserUpdateForm, DepartmentCreationForm, TeamCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Profile, Department, Team
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer, DepartmentSerializer, TeamSerializer

def NewName(newname):
    i = 1
    New_User = newname
    AllUsers = User.objects.values_list('username', flat=True).all()
    for oneuser in AllUsers:
        while New_User == oneuser:
            New_User = newname + str(i)
            i += 1
    return New_User

def DepCodeIsUnique(depcode):
    dep = Department.objects.values_list('dep_code', flat = True).all()
    if depcode in dep:
        return True
    else:
        return False

def TeamCodeIsUnique(tmcode):
    tm = Team.objects.values_list('team_code', flat = True).all()
    if tmcode in tm:
        return True
    else:
        return False

# All routes related to user creation and update...
def register(request):
    prf = Profile.objects.get(user__username = request.user.username)
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
                pro = Profile(user = usr, role = form2.cleaned_data.get('role'), department = form2.cleaned_data.get('department'), team = form2.cleaned_data.get('team'))
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
            'form2': form2,
            'prf': prf
        }
    return render(request, 'dre_admin/register_user.html', context)

@login_required
def UpdateUser(request, uid):
    usr = User.objects.filter(username = uid).first()
    prf = Profile.objects.filter(user__username = uid).first()
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
                prf.department = form2.cleaned_data.get("department")
                prf.team = form2.cleaned_data.get("team")
                prf.save()
                messages.success(request, 'User was successfully updated')
                return redirect('register_user') 
            except Exception as e:
                messages.error(request, str(e))
                return redirect('register_user')
    else:
        #form1 = UserRegisterForm()
        #form2 = UserProfileCreationForm()
        pass
    return redirect('register_user')

@login_required
def profile(request, uid):
    prf = Profile.objects.get(user__username = request.user.username)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST)
        usr = User.objects.get(username = uid)
        if u_form.is_valid():
            try:
                usr.first_name = u_form.cleaned_data.get('first_name')
                usr.last_name = u_form.cleaned_data.get('last_name')
                usr.email = u_form.cleaned_data.get('email')
                usr.save()
                messages.success(request, '{} profile was successfully updated :)'.format(uid))
            except Exception as e:
                messages.error(request, str(e))
    else:
        u_form = UserUpdateForm()
        
    context = {'u_form': u_form, 'uid': uid, 'prf': prf}
    return render(request, 'dre_admin/profile.html', context)

@login_required
def change_password(request, uid):
    prf = Profile.objects.get(user__username = request.user.username)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            try:
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
            except Exception as e:
                messages.error(request, str(e))
        else:
            messages.error(request, 'Please correct the error above.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'dre_admin/change_password.html', {
        'form': form, 'uid': uid, 'prf': prf
    })


@login_required
def Departments(request):
    prf = Profile.objects.get(user__username = request.user.username)
    deps = Department.objects.all().order_by('id')
    if request.method == 'POST':
        form = DepartmentCreationForm(request.POST)
        if form.is_valid():
            try:
                check_dep_code = DepCodeIsUnique(form.cleaned_data.get('dep_code'))
                if check_dep_code:
                    messages.error(request, 'Department code already exists')
                else:
                    dep = Department(dep_code = form.cleaned_data.get('dep_code'), 
                    dep_name = form.cleaned_data.get('dep_name'),
                    dep_description = form.cleaned_data.get('dep_description'))
                    dep.save()
                    messages.success(request,'New department was successfully created :)')
            except Exception as e:
                messages.error(request, str(e))
    else:
        form = DepartmentCreationForm()
    context = {
        'form': form,
        'deps': deps,
        'prf': prf
    }
    return render(request, 'dre_admin/department.html', context)

@login_required
def UpdateDepartment(request, did):
    dep = Department.objects.get(id = did)
    if request.method == 'POST':
        form = DepartmentCreationForm(request.POST)
        if form.is_valid():
            try:
                check_dep_code = DepCodeIsUnique(form.cleaned_data.get('dep_code'))
                if check_dep_code and form.cleaned_data.get("dep_code") != dep.dep_code:
                    messages.error(request, 'Department code already exists')
                else:
                    dep.dep_code = form.cleaned_data.get("dep_code")
                    dep.dep_name = form.cleaned_data.get("dep_name")
                    dep.dep_description = form.cleaned_data.get("dep_description")
                    dep.save()
                    messages.success(request, 'Department was successfully updated :)')
            except Exception as e:
                messages.error(request, str(e))
        else:
            messages.error(request, form)
    return redirect('departments')
    
@login_required
def Teams(request):
    prf = Profile.objects.get(user__username = request.user.username)
    teams = Team.objects.all().order_by('id')
    if request.method == 'POST':
        form = TeamCreationForm(request.POST)
        if form.is_valid():
            try:
                tm = Team(team_code = form.cleaned_data.get('team_code'),
                            team_name = form.cleaned_data.get('team_name'),
                            team_description = form.cleaned_data.get('team_description'),
                            team_dep = form.cleaned_data.get('team_dep'))
                tm.save()
                messages.success(request,'New team was successfully created :)')
            except Exception as e:
                messages.error(requeset, str(e))
    else:
        form = TeamCreationForm()

    context = {
        'prf': prf,
        'teams': teams,
        'form': form
    }
    return render(request, 'dre_admin/teams.html', context)

@login_required
def UpdateTeam(request, tid):
    tm = Team.objects.get(id = tid)
    if request.method == 'POST':
        form = TeamCreationForm(request.POST)
        if form.is_valid():
            try:
                check_team_code = TeamCodeIsUnique(form.cleaned_data.get('team_code'))
                if check_team_code and form.cleaned_data.get('team_code') != tm.team_code:
                    messages.error(request, 'Team code already exists')
                else:
                    tm.team_code = form.cleaned_data.get('team_code')
                    tm.team_name = form.cleaned_data.get('team_name')
                    tm.team_description = form.cleaned_data.get('team_description')
                    tm.team_dep = form.cleaned_data.get('team_dep')
                    tm.save()
                    messages.success(request, 'Team was successfully updated:)') 
            except Exception as e:
                messages.error(request, str(e))
    return redirect('teams')

# REST API VIEWS...

@login_required
@api_view(['GET'])
def GetAllUsers(request):
    prf = Profile.objects.all().order_by('user__id')
    serializer = ProfileSerializer(prf, many = True)
    return Response(serializer.data)

@login_required
@api_view(['GET'])
def GetUserByID(response, uid):
    prf = Profile.objects.get(user__username = uid)
    serializer = ProfileSerializer(prf, many = False)
    return Response(serializer.data)

@login_required
@api_view(['GET'])
def GetAllDepartments(request):
    deps = Department.objects.all().order_by('id')
    serializer = DepartmentSerializer(deps, many = True)
    return Response(serializer.data)

@login_required
@api_view(['GET'])
def GetDepartmentByID(request, did):
    dep = Department.objects.get(id = did)
    serializer = DepartmentSerializer(dep, many = False)
    return Response(serializer.data)

@login_required
@api_view(['GET'])
def GetAllTeams(request):
    tms = Team.objects.all().order_by('id')
    serializer = TeamSerializer(tms, many = True)
    return Response(serializer.data)

@login_required
@api_view(['GET'])
def GetTeamByID(request, tid):
    tms = Team.objects.get(id = tid)
    serializer = TeamSerializer(tms, many = False)
    return Response(serializer.data)


