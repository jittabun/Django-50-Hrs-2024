from django.shortcuts import render
from django.http import HttpResponse
from .models import Tracking

# Create your views here.
def Home(request):
    return render(request,'myapp/home.html')

def Aboutus(request):
    return render(request,'myapp/aboutus.html')

def Contact(request):
    return render(request,'myapp/contact.html')

def TrackingPage(request):
    tracks = Tracking.objects.all()
    context = {'tracks':tracks}
    return render(request,'myapp/tracking.html',context)

def Sawatdee(requests):
    return HttpResponse("<h1>สวัสดีจ้าา</h1>")

