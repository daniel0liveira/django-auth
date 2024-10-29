from xml.etree.ElementInclude import include

from django.contrib.auth.decorators import login_required
from django.urls import path

from home.views import *

urlpatterns =[
    path('',index,name='home'),
]