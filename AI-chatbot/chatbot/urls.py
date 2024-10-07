from django.urls import path
from . import views  # Ensure this import is correct

urlpatterns = [

    path('', views.chatbot, name='chatbot'),  # Ensure 'views.chatbot' matches the function name in views.py
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
