
from django.urls import path, include

from .views import *

urlpatterns = [
    path('',posts,name='posts'),
    
]


# handler404 = "home.views.bad_request"