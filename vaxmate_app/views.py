from django.shortcuts import render


def home(request):
    return render(request, "htmlpages/home.html")

def features(request):
    return render(request, "htmlpages/features.html")

def about(request):
    return render(request, "htmlpages/about.html")

def contact(request):
    return render(request, "htmlpages/contact.html")

def register(request):
    return render(request, "htmlpages/register.html")

def login_page(request):
    return render(request, "htmlpages/login.html")

def profile(request):
    return render(request, "htmlpages/profile.html")

def dashboard(request):
    return render(request, "htmlpages/dashboard.html")

def reminder(request):
    return render(request, "htmlpages/reminder.html")

def vaccine_schedule(request):
    return render(request, "htmlpages/vaccineschedule.html")

def verify_email(request):
    return render(request, "htmlpages/verifyemail.html")

def centers(request):
    return render(request, "htmlpages/center.html")

