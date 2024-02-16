from django.urls import path
# from .views import Home, Sawatdee, Aboutus, Contact, Tracking
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('aboutus', Aboutus, name='about-us'),
    path('contact', Contact, name='contact'),
    path('tracking', TrackingPage, name='tracking'),
    path('sawatdee', Sawatdee),
]
