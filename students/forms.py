from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from exam.models import Student
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.forms import StudentCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _


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

SEMESTER = (
        ("1st Semester", "1st Semester"),
        ("2nd Semester", "2nd Semester"),
    )

COURSE = (
        ("Choose a course", "Choose a course"),
        ("COS203", "COS203"),
        ("COS203", "COS203"),
        ("COS461", "COS461"),
    )


LEVEL = (
        ("100", "100"),
        ("200", "200"),
        ("300", "300"),
        ("400", "400"),
    )


class StudentRegisterForm(StudentCreationForm):
    id = forms.CharField(label='Matric No', max_length=20)
    name = forms.CharField(label='Name', max_length=100)
    sex = forms.ChoiceField(choices=SEX)
    dept = forms.ChoiceField(choices=DEPT)
    major = forms.ChoiceField(label='Major', choices=DEPT)
    email = forms.EmailField()
    birth = forms.DateField()


    class Meta:
        model = Student
        fields = [
            'id',
            'name',
            'sex',
            'dept',
            'major',
            'email',
            'birth',
            'password1',
            'password2'
        ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'image'
        ]


class ContactForm(forms.Form):
    # yourname = forms.CharField(max_length=100, required=False, label='Your Name')
    # email = forms.EmailField(required=False, label='Your Email Address')
    semester = forms.ChoiceField(choices=SEMESTER, required=False, label='Semester', help_text="Select your semester")
    course = forms.ChoiceField(choices=COURSE, required=False, label='Course', initial=None, help_text="Choose the course you wish to offer")
    level = forms.ChoiceField(choices=LEVEL, required=False, label='Choose your level')

    class Meta:
        # model = Student
        fields = [
            'semester',
            'course',
            'level',
        ]


class LoginForm(AuthenticationForm):
    # yourname = forms.CharField(max_length=100, required=False, label='Your Name')
    # email = forms.EmailField(required=False, label='Your Email Address')
    stuid = forms.ChoiceField(widget=TextInput(attrs={'placeholder':'matric no'}))
    password = forms.ChoiceField(widget=PasswordInput(attrs={'placeholder':'matrkic no'}))

    class Meta:
        # model = Student
        fields = [
            'stuid',
            'password',
        ]