from django import forms
from django.contrib.auth.models import User
from exam.models import Teacher
from django.db import models
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import TeacherCreationForm


DEPT = (
        ("Maths_&_Comp", "Maths and Computer Science"),
        ("BioChem", "BioChemistry"),
        ("Accounting", "Accounting"),
        ("Economics", "Economics"),
        ("History", "History"),
        ("Mass Commuication", "Mass Commuication"),
    )

SEX = (
        ("Male", "Male"),
        ("Female", "Female"),
    )


class TeacherRegisterForm(TeacherCreationForm):
    # id = forms.CharField(label='Teacher ID', max_length=20)
    name = forms.CharField(label='Name', max_length=100)
    username = forms.CharField(label='Username', max_length=50)
    sex = forms.ChoiceField(choices=SEX)
    dept = forms.ChoiceField(choices=DEPT)
    email = forms.EmailField()

    class Meta:
        model = Teacher
        fields = [
            # 'id',
            'name',
            'username',
            'sex',
            'dept',
            'email',
            'password1',
            'password2'
        ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'image'
        ]