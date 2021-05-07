from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from exam.models import models
from .forms import ExamCreateForm
from django.db import models
from django.views.generic import ListView, CreateView
from exam.models import Student, Paper, Teacher, Exam
from django.contrib.auth.decorators import login_required
# Import ListView module
from django.views.generic import ListView
# Import Q module
from django.db.models import Q


# from django.contrib.auth.forms import UserCreationForm
from .forms import TeacherRegisterForm
from django.contrib import messages
# from django.contrib.auth import login, authenticate


def register(request):
    if request.method == 'POST':
        form = TeacherRegisterForm(request.POST)
        # username: ''
        if form.is_valid():
            form.save()
            username: form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now login')
            # return render(request, 'lecturers/login.html')
            return redirect('lecturer-login')
    else:
        form = TeacherRegisterForm()
    return render(request, 'lecturers/register.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = TeacherRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             name: form.cleaned_data.get('name')
#             username: form.cleaned_data.get('username')
#             sex: form.cleaned_data.get('sex')
#             dept: form.cleaned_data.get('dept')
#             email: form.cleaned_data.get('email')
#             birth: form.cleaned_data.get('birth')
#             # password: form.cleaned_data.get('password1')
#             user = authenticate(name=name, username=username,  sex=sex, dept=dept, email=email, birth=birth)
#             messages.success(request, f'Account Created for {username}!')
#             login(request, user)
#         return render(request, 'lecturers/dashboard.html')
#     else:
#         form = TeacherRegisterForm()
#         return render(request, 'lecturers/register.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = TeacherRegisterForm(request.POST)
#         form.save()

#         # if form.is_valid():
#         #     form.save()
#         #     username = form.cleaned_data.get('username')
#         #     messages.success(request, f'Account Created for {username}!')
#         #     return redirect('exam-home')
#         return render(request, 'lecturers/register.html')
#     else:
#         # form = TeacherRegisterForm()
        
#         return render(request, 'lecturers/dashboard.html')
#     # return render(request, 'lecturers/register.html', {'form': form})

# @login_required
# def dashboard(request):
#     # teacher = get_object_or_404(Teacher)
#     # teacher = teacher.username
#     return render(request, 'lecturers/dashboard.html', {'title': 'Dashboard'})


# Define class for Querying data
class dashboard(ListView):
    # Define model
    model = Student
    # Define template
    template_name = 'lecturers/dashboard.html'
    # context_object_name = 'teacher'


    def get_queryset(self):
        # Set the default query set
        queryset = Student.objects.all()
        # Check the form value is submitted or not
        if self.request.GET.keys():
            # Check the search keyword
            if self.request.GET.get('src') != '':
                keyword = self.request.GET.get('src')
                # Set the query set based on search keyword
                queryset = Student.objects.filter(Q(brand=keyword.capitalize()) | Q(type=keyword.capitalize()))
        return queryset



def login(request):
    return render(request, 'lecturers/login.html', {'title': 'Login'})



def teacherLogin(request):
    if request.method == 'POST':
        # teaId = request.POST.get('id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print("id", teaId, "username", username, "password", password)
        print("username", username, "password", password)

        teacher = Teacher.objects.get(username=username)
        # teachers = Teacher.objects.filter(id=teacher.id)
        print(teacher)
        if (password == teacher.password1) and (username == teacher.username): 
            # paper = Paper.objects.filter(tid=teacher.id)
            messages.success(request, f'You successfully logged in')
            # return render(request,'lecturers/dashboard.html', {'teacher':teacher})
            return redirect(reverse('lecturer_dashboard'), {'teacher':teacher})
    else: 
        return render (request, 'exam/about.html', {'message': 'Incorrect password'})


def profile(request):
    return render(request, 'lecturers/profile.html', {'title': 'UserProfile'})


class ExamCreateView(CreateView):
    model = Exam
    form_class = ExamCreateForm
    template_name = 'lecturers/exam_form.html'

    def form_valid(self, form):
        form.instance.lecturer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('exam-create')

   
    # def get_absolute_url(self): # new
    #     return reverse('exam-create', args=[str(self.id)])


# def studentLogin(request):
#     if request.method=='POST':
# # Get form information
#         stuId=request.POST.get('id')
#         password=request.POST.get('password')
#         print("id",stuId,"password",password)
# # Get the student entity by student number
#         student=models.Student.objects.get(id=stuId)
#         print(student)
#         if password == student.password: #Login successful
#     #Query test information
#             paper=models.Paper.objects.filter(major=student.major)
# #Query score information
#             grade=models.Grade.objects.filter(sid=student.id)
#     # render index template
#         return render(request,'index.html',{'student':student,'paper':paper,'grade':grade})

#     else: return render (request, 'index.html', {'message': 'Incorrect password'})