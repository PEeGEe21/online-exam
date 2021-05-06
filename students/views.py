from django.shortcuts import render, redirect, reverse, get_object_or_404, resolve_url
from django.contrib import messages
from exam.models import Student, Paper, Teacher, Exam, Grade
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from exam.models import models
from django.db import models
from .forms import StudentRegisterForm
from .forms import ContactForm, LoginForm
from django.contrib import messages
from django.contrib.auth.views import LoginView

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'students/demo.html')


def result(request):
    return render(request, 'students/result.html')




# def info(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         # username: ''
#         if form.is_valid():
#             form.save()
#             name: form.cleaned_data.get('name')
#             messages.success(request, f'Your account has been created! You can now login')
#             # return render(request, 'students/login.html')
#             return redirect('students-login')
#     else:
#         form = ContactForm()
#     return render(request, template_name="students/start_exam.html", context={'form': form})

# def login(request):
#     return render(request, 'students/login.html')


# def startExam(request):
#     return render(request, 'students/start_exam.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        # username: ''
        if form.is_valid():
            form.save()
            name: form.cleaned_data.get('name')
            messages.success(request, f'Your account has been created!')
            # return render(request, 'students/login.html')
            return redirect('students-login')
    else:
        form = StudentRegisterForm()
    return render(request, 'students/register.html', {'form': form})

# def studentLogin(request):
#     if request.method == "POST":
#         form = AuthenticationLoginForm(request, data=request.POST)
#         if form.is_valid():
#             print ("Hello world")
#             name = form.cleaned_data.get('id')
#             password = form.cleaned_data.get('password')
#             user = authenticate(name=name, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as")
#                 return redirect("main:homepage")
#             else:
#                 messages.error(request,"Invalid Matric No.")
#         else:
#             print ("Fuck off")
#             messages.error(request,f'Print Error')
#     form = AuthenticationLoginForm()
#     return render(request=request, template_name="students/login.html", context={"form":form})

# def studentLogin(request):
#     # context = RequestContext(request)
#     if request.method == 'POST':
#         stuId = request.POST.get('reg_no')
#         password = request.POST.get('password')
#         print("reg_no",stuId,"password",password)
#         user = authenticate(stuId=stuId, password=password)
#         student = Student.objects.get(id=stuId)
#         if (user is not None) and (password == student.password):
#             if user.is_active:
#                 login(request, user)
#                 messages.info(request, f'You are now logged in as')
#                 return HttpResponseRedirect("exam/home")
#             else:
#                 messages.error(request,"Invalid Matric No.")
#         else:
#             print ("invalid login details" + stuId + " " + password)
#             messages.success(request, f'You are logged in ')
#             return render(request, 'students/start_exam.html', {'student':student})
#     else:
#         return render(request, 'students/login.html', {'message': 'Incorrect password'})


    
        
# if (password == student.password):
#             messages.success(request, f'You are ')
#             return render(request, 'students/start_exam.html', {'student':student})

#         else:
#             print ("invalid login details" + stuId + " " + password)
#             messages.success(request, f'You are ')
#             return render(request, 'students/login.html', {'student':student})

# def studentLogin(request):
#     if request.method == 'POST':
#         stuId = request.POST.get('reg_no')
#         password = request.POST.get('password')
#         student = authenticate(request, stuId=stuId, password=password)
#         print(student)
#         if student is not None:
#             studentlogin(request, student)
#             messages.success(request, f'{stuId}, You are logged in! ')  
#             return render(request,'students/start_exam.html')
#         else:
#             return render (request, 'exam/about.html', {'message': 'Incorrect password'})

# class MyLoginView(LoginView):
#     authentication_form = LoginForm
#     template_name = 'students/login.html'
#     redirect_authenticated_user = True

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         msg = {'uhuhujhkhkhkhku'}
#         context['msg'] = msg.get(self.request.GET.get('kjjijkjkj'), '')
#         return context

#     def get_success_url(self):
#         return resolve_url('startexam')

def studentLogin(request):
    if request.method=='POST':
        stuId = request.POST.get('reg_no')
        password = request.POST.get('password')
        print("reg_no",stuId,"password",password)
        student = Student.objects.get(id=stuId)
        print(student)
        form = ContactForm(request.POST)
        
        if password == student.password1: #Login successful

    # #Query test information
            # paper = Paper.objects.get(Tid=student.id)
            # paper = Paper.objects.filter(major=student.major)
    # #Query score information
            # grade = Grade.objects.filter(sid=student.id)
    # # render index template
            # return HttpResponseRedirect(reverse('startexam', kwargs={'student':student}))
            messages.success(request, f'Welcome, {stuId}! You are logged in! ')
            
            return render(request,'students/start_exam.html', {'student':student, 'form':form})
            # return redirect(reverse('startexam', kwargs={'student':student}))
            # return redirect('startexam')

    else: 
        return render (request, 'exam/about.html', {'message': 'Incorrect password'})

        
def examstart(request):
    if request.method=='POST':
        messages.success(request, f'You are logged In stuId')
        return redirect('exam-home')

    else: 
        return render (request, 'exam/about.html', {'message': 'Incorrect password'})

# def startExam(request):
#     student = get_object_or_404(Student)
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         # username: ''
#         # if form.is_valid():
#         #     form.save()
#         #     name: form.cleaned_data.get('name')
#         #     messages.success(request, f'Your account has been created! You can now login')
#         #     # return render(request, 'students/login.html')
#         #     return redirect('students-login')
#     else:
#         form = ContactForm()
#     return render(request, template_name="students/start_exam.html", context={'form': form, 'student':student})