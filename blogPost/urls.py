
from django.urls import path, include

from .views import *

urlpatterns = [
    path('',posts,name='posts'),
    path('<slug>/',blog_detail,name='blog_detail'),
    
]


# handler404 = "home.views.bad_request"