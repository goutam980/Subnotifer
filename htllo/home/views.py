from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")
def home(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
def services(request):
    context={
        'vari': "this is sent from the django app  "
    }
    return render(request, "services.html",context)