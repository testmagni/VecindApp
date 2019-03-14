from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    """ class for homepage """
    print(request.user.user_resident.property_relation)
    return HttpResponse('Welcome to the homepage {}'.format(request.user.user_role))
