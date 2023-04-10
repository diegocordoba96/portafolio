from django.urls import path
from  project_portafolio import views

urlpatterns = [
    path('', views.home, name='home')

]