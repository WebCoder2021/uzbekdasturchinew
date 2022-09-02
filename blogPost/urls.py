
from django.urls import path, include

from .views import *

urlpatterns = [
    path('',posts,name='posts'),
    path('<slug>/',blog_detail,name='blog_detail'),
    path('like/<slug>/',blog_like,name='blog_like'),
    path('dislike/<slug>/',blog_dislike,name='blog_dislike'),
    
]


# handler404 = "home.views.bad_request"