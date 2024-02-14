from django.urls import path
from .views import Home, Sawatdee, Aboutus, Contact

urlpatterns = [
    path('', Home, name='home'),
    path('aboutus', Aboutus, name='about-us'),
    path('contact', Contact, name='contact'),
    path('sawatdee', Sawatdee),
]
