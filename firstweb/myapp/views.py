from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request,'myapp/home.html')

def Aboutus(request):
    return render(request,'myapp/aboutus.html')

def Contact(request):
    return render(request,'myapp/contact.html')

def Tracking(request):
    tracks = ['Pom - TA312321','Sarah - TA312322','James - TA312323','Olate - TA312324']
    context = {'tracks':tracks}
    return render(request,'myapp/tracking.html',context)

def Sawatdee(requests):
    return HttpResponse("<h1>สวัสดีจ้าา</h1>")

