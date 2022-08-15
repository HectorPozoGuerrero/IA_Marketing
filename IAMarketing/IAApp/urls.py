from django.urls import path
from IAApp import views


urlpatterns = [

    
    path('', views.iaHomeView, name= 'iaHomeUrl'),
    path('aboutus/', views.aboutUsView, name= 'aboutUsUrl'),
    path('project/', views.projectView, name= 'projectUrl'),
    path('example/', views.exampleView, name= 'exampleUrl'),
    path('projectFirstStep', views.projectFirstStep, name="projectFirstStep")

]
