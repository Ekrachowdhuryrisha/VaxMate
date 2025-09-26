import random, time
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse


def home(request):
    return render(request, "htmlpages/home.html")

def features(request):
    return render(request, "htmlpages/features.html")

def aboutUs(request):
    return render(request, "htmlpages/aboutUs.html")

def contact(request):
    return render(request, "htmlpages/contact.html")


# 🔹 Helper function: send OTP
def send_otp(request, email):
    otp = str(random.randint(100000, 999999))  # generate 6-digit otp
    request.session['otp'] = otp
    request.session['email'] = email
    request.session['otp_time'] = time.time()  # store OTP generation time

    try:
        send_mail(
            subject="Your VaxMate Verification Code",
            message=f"Your verification code is {otp}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )
    except Exception as e:
        print("Email sending failed:", e)
        messages.error(request, "Could not send OTP. Try again later.")


# 🔹 Register view
def register(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("reset_password")

        # password match check
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "htmlpages/register.html")

        # check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, "htmlpages/register.html")

        # temporarily store user info
        request.session['temp_user'] = {
            "full_name": full_name,
            "email": email,
            "password": password,  # kept until OTP verified
        }

        # send OTP
        send_otp(request, email)
        return redirect("verify")  # go to verification page

    return render(request, "htmlpages/register.html")


# 🔹 Verify view
def verify(request):
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "submit":
            entered_otp = request.POST.get("otp")
            saved_otp = request.session.get("otp")
            otp_time = request.session.get("otp_time")

            # check expiry (5 minutes)
            if otp_time and time.time() - otp_time > 300:
                return render(request, "htmlpages/verify.html", {"error": "OTP expired. Please resend."})

            if entered_otp == saved_otp:
                data = request.session.get("temp_user")

                if data:
                    # create user
                    user = User.objects.create_user(
                        username=data["email"],  # username as email
                        email=data["email"],
                        password=data["password"],
                        first_name=data["full_name"]
                    )
                    user.save()

                    # clear session
                    for key in ["otp", "otp_time", "temp_user", "email"]:
                        if key in request.session:
                            del request.session[key]

                    messages.success(request, "Account created successfully! Please log in.")
                    return redirect("login")  # go to login page
            else:
                return render(request, "htmlpages/verify.html", {"error": "Wrong code"})

        elif action == "resend":
            email = request.session.get("email")
            if email:
                send_otp(request, email)
                return render(request, "htmlpages/verify.html", {"error": "A new OTP has been sent"})
            else:
                return redirect("register")

    return render(request, "htmlpages/verify.html")


# 🔹 Login view
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")  # in our case, email
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Django session login
            return redirect("dashboard")  # ✅ redirect to dashboard
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "htmlpages/login.html")


@login_required(login_url='login')
def dashboard(request):
    return render(request, "htmlpages/dashboard.html")


def logout_view(request):
    logout(request)
    return redirect("home")


def profile(request):
    return render(request, "htmlpages/profile.html")

def reminder(request):
    return render(request, "htmlpages/reminder.html")

def vaccine_schedule(request):
    return render(request, "htmlpages/vaccineschedule.html")

def verify_email(request):
    return render(request, "htmlpages/verifyemail.html")

def centers(request):
    return render(request, "htmlpages/center.html")


# 🔹 Contact form (authority email message)
def send_message(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            f"New Message from {name}",
            message,
            email,  # Sender's email
            [settings.AUTHORITY_EMAIL],  # Replace with authority's email
        )

        return HttpResponse("Thank you for contacting us! We will get back to you soon.")
    return redirect('home')
