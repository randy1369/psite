from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'portfolio/index.html')

def xfiles(request):
    return render(request, 'portfolio/x.html')

def blog(request):
    return render(request, 'portfolio/blog.html')

def bookLib(request):
    return render(request, 'portfolio/books.html')

def Cdashboard(request):
    return render(request, 'portfolio/cdashboard.html')

def videoS(request):
    return render(request, 'portfolio/vs.html')

def ecom(request):
    return render(request, 'portfolio/ecom.html')

def scraper(request):
    return render(request, 'portfolio/scraper.html')