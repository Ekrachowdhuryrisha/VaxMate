from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile', 'gender', 'date_of_birth', 'profession', 'address', 'blood_group', 'photo']
