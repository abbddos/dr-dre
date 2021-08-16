from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#from django.contrib.auth.models import User
from dre_admin.models import Profile

@login_required()
def home(request):
    prf = Profile.objects.get(user__username = request.user.username)
    context = {'prf' : prf}
    return render(request, 'home/home.html', context)
