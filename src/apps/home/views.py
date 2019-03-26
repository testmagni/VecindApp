from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    """ function for homepage """
    # print(request.user.r_profile.property_relation)
    return render(request, 'home/home.html')
