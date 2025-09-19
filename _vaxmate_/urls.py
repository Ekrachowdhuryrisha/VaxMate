"""
URL configuration for _vaxmate_ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vaxmate_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Pages
    path('', views.home, name='home'),
    path('features/', views.features, name='features'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reminder/', views.reminder, name='reminder'),
    path('vaccineschedule/', views.vaccine_schedule, name='vaccineschedule'),
    path('verifyemail/', views.verify_email, name='verifyemail'),
    path('centers/', views.centers, name='centers'),
]
