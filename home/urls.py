
from django.urls import path, include

from .views import *

urlpatterns = [
    path('',main,name='main'),
    
]


# handler404 = "home.views.bad_request"