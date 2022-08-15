from django.urls import include, path
from LoginApp import views

urlpatterns = [
    
    path('register/', views.registerView, name='registerUrl')
    ]
