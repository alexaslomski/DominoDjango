from django.urls import path, include
from . import views as user_views

urlpatterns = [

path('register/', user_views.register, name='users-register'),

]