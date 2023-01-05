from django.contrib import admin
from django.urls import path, include
from home import views

#Admin side customisation
admin.site.site_header= "Welcome to Shubham's Dashboard"
admin.site.site_title= "Portfolio Admin"
admin.site.index_title= "Welcome to the Portal"


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
    path('contactA', views.contactA, name='contactA'),
]
