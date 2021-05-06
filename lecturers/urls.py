from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [
    path('register/', views.register, name='lecturer_register'),
    # path('login/', views.login, name='lecturer-login'),
    path('login/', auth_views.LoginView.as_view(template_name='lecturers/login.html'), name='lecturer-login'),
    url(r'^teacherLogin/', views.teacherLogin, name='teacherLogin'),
    path('create/', views.ExamCreateView.as_view(), name='exam-create'),
    path('profile/', views.profile, name='lecturer-profile'),

    path('dashboard/', views.dashboard.as_view(template_name='lecturers/dashboard.html'), name='lecturer_dashboard'),
]