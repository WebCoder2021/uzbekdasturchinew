from django.urls import path
from .views import *
urlpatterns = [
    path('', log_in,name='login'),
    path('logout/', logout_view,name='logout'),
    path('check_user/', check_user,name='check_user'),
    path('settings/', settings, name="settings"),
    path('profile/', profile, name="profile"),
]