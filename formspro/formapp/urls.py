from django.urls import path
from formapp import views

urlpatterns = [
    path('', views.homepage,name='home'),
    path('register',views.createEmp,name='register'),

]