from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_register, name='register'),
    path('login/', views.login_view, name='login'),

]
