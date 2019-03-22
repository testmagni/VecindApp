from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    """ class for homepage """
    # print(request.user.r_profile.property_relation)
    if request.user.role == 1:
        msg = ' y eres un residente'
    elif request.user.role == 2:
        msg = ' y eres un vigilante'
    return HttpResponse('Welcome to the homepage {0}, {1}'.format(request.user.username, msg))
