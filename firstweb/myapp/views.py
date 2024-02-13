from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(requests):
    return HttpResponse("<h1>Hello World</h1>")

def Sawatdee(requests):
    return HttpResponse("<h1>สวัสดีจ้าา</h1>")
    