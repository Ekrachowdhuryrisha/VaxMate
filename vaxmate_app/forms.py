from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile', 'gender', 'date_of_birth', 'profession', 'address', 'blood_group', 'photo']
from .models import FamilyMember

class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        fields = ["name", "age", "relation", "vaccine_name", "date_time", "notification_type"]

        widgets = {
            "date_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
