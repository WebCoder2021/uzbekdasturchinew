
from django.urls import path, include

from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('faq/',faq,name='faq'),
    
]


# handler404 = "home.views.bad_request"