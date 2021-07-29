from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import studyUser, Session, part_1, part_2, part_3

# Sona ID Form
class studyUserForm(forms.ModelForm):
    class Meta:
        fields = ['sonaID',]
        model = studyUser

# Trial 1 Form
class part_1Form(forms.ModelForm):
    class Meta:
        fields = ['name','age','major',]
        model = part_1

# Trial 2 Form
class part_2Form(forms.ModelForm):
    class Meta:
        fields = ['advanced_degree', 'dream_Job',]
        model = part_2

# Trial 3 Form
class part_3Form(forms.ModelForm):
    class Meta:
        fields = ['user_os','user_phone','phone_sat',]
        model = part_3