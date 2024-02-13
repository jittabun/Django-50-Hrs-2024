from django.urls import path
from .views import Home, Sawatdee

urlpatterns = [
    path('',Home),
    path('sawatdee', Sawatdee),
]
