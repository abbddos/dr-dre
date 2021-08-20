from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer, Job
from dre_admin.models import Profile
from .forms import CustomerCreationForm, JobCreationForm
from .serializers import CustomerSerializer, JobSerializer
from django.http import FileResponse
import pandas as pd


def IsJobCodeUnique(jobcode):
    JC = Job.objects.values_list('code', flat = True).all()
    if jobcode in JC:
        return False
    else:
        return True

@login_required
def Customers(request):
    prf = Profile.objects.get(user__username = request.user.username)
    customers = Customer.objects.all().order_by('id')
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            try:
                CST = Customer(name = form.cleaned_data.get('name'),
                                email = form.cleaned_data.get('email'),
                                phone_number = form.cleaned_data.get('phone_number'),
                                ride = form.cleaned_data.get('ride'),
                                RegisterDate = datetime.today())
                CST.save()
                messages.success(request, 'New customer was successfully created :)')
                return redirect('customers')
            except Exception as e: 
                messages.error(request, str(e))
                return redirect('customers')
    else:
        form = CustomerCreationForm()

    context = {
        'prf': prf,
        'form': form,
        'customers': customers
    }
    return render(request, 'dre_jobs/customers.html', context)

@login_required
def UpdateCustomer(request, cid):
    cstmr = Customer.objects.get(id = cid)
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            try:
                cstmr.name = form.cleaned_data.get('name')
                cstmr.email = form.cleaned_data.get('email')
                cstmr.phone_number = form.cleaned_data.get('phone_number')
                cstmr.ride = form.cleaned_data.get('ride')
                cstmr.save()
                messages.success(request, 'Customer was successfully updated :)')
            except Exception as e:
                messages.error(request, str(e))
    else:
        pass
    return redirect('customers')

@login_required
def Jobs(request):
    prf = Profile.objects.get(user__username = request.user.username)
    jbs = Job.objects.all().order_by('id')
    if request.method == 'POST':
        form = JobCreationForm(request.POST) 
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Job was successfully added :)') 
            except Exception as e:
                messages.error(request, str(e))
    else:
        form = JobCreationForm()
    context = {
        'prf': prf,
        'jbs': jbs, 
        'form': form
    }
    return render(request, 'dre_jobs/jobs.html', context)

@login_required
def UpdateJob(request, jid):
    jbs = Job.objects.get(id = jid)
    if request.method == 'POST':
        form = JobCreationForm(request.POST)
        if form.is_valid():
            try:
                CheckJBCode = IsJobCodeUnique(form.cleaned_data.get('code'))
                if not CheckJBCode and form.cleaned_data.get('code') != jbs.code:
                    messages.error(request, 'Job Code already exists, try another one...')
                    return redirect('jobs')
                else:
                    jbs.code = form.cleaned_data.get('code')
                    jbs.description = form.cleaned_data.get('description')
                    jbs.start_date = form.cleaned_data.get('start_date')
                    jbs.end_date = form.cleaned_data.get('end_date')
                    jbs.status = form.cleaned_data.get('status')
                    jbs.department = form.cleaned_data.get('department')
                    jbs.team = form.cleaned_data.get('team')
                    jbs.customer = form.cleaned_data.get('customer')
                    jbs.save()
                    messages.success(request, 'Job was successfully updated')
                    return redirect('jobs')
            except Exception as e:
                messages.error(request, str(e))
                return redirect('jobs')
    else:
        pass
    return redirect('jobs')

@login_required
def GetJobsData(request):
    df = pd.read_json('http://localhost:8000/dre_jobs/GetAllJobs/')
    df1 = pd.DataFrame()
    df1['id'] = df.id
    df1['Code'] = df.code
    df1['Description'] = df.description
    df1['Start Date'] = df.start_date
    df1['End Date'] = df.end_date
    df1['Status'] = df.status

    deps = []
    tems = []
    cust = []
    ride = []

    for i in range(len(df)):
        deps.append(df['department'][i]['dep_name'])
        tems.append(df['team'][i]['team_name'])
        cust.append(df['customer'][i]['name'])
        ride.append(df['customer'][i]['ride'])

    df1['Department'] = deps
    df1['Team'] = tems
    df1['Customer'] = cust
    df1['Ride'] = ride
    file = df1.to_csv()
    response = FileResponse(file)
    response['Content-type'] = 'text/csv'
    response['Content-Disposition'] = 'attachment; filename= Jobs_data.csv'
    return response

# RESTFUL API...

@login_required
@api_view(['GET'])
def GetAllCustomers(request):
    customers = Customer.objects.all().order_by('id')
    serializer = CustomerSerializer(customers, many = True)
    return Response(serializer.data)

@login_required
@api_view(['GET'])
def GetCustomerByID(request, cid):
    cstmr = Customer.objects.get(id = cid)
    serializer = CustomerSerializer(cstmr, many = False)
    return Response(serializer.data)

#@login_required
@api_view(['GET'])
def GetAllJobs(request):
    jobs = Job.objects.all().order_by('id')
    serializer = JobSerializer(jobs, many = True)
    return Response(serializer.data)

@login_required
@api_view(['GET'])
def GetJobByID(request, jid):
    jb = Job.objects.get(id = jid)
    serializer = JobSerializer(jb, many = False)
    return Response(serializer.data)

