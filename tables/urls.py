from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('student/',views.student, name = 'student'),
    path('warden/',views.warden, name = 'warden'),
    path('room/',views.room, name = 'room'),
    path('block/',views.block, name = 'block'),
    path('mess/',views.mess, name = 'mess'),
    path('parent/',views.parent, name = 'parent'),
    path('retrieve/',views.retrieve, name = 'retrieve'),
    path('delete/',views.delete, name = 'delete'),
    path('update/',views.update,name='update'),

]