from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from . import views


urlpatterns = [

    path('home/', views.home, name='tfb-home'),
    path('domino_view_become_leader/', views.domino_view_become_leader, name='tfb-domino_view_become_leader'),
    path('domino_view_get_the_emblem/', views.domino_view_get_the_emblem, name='tfb-domino_view_get_the_emblem'),
    path('domino_view_community_guidelines/', views.domino_view_community_guidelines, name='tfb-domino_view_community_guidelines'),
    path('domino_view_contact/', views.domino_view_contact, name='tfb-domino_view_contact'),
    path('domino_view_cookie_policy/', views.domino_view_cookie_policy, name='tfb-domino_view_cookie_policy'),
    path('domino_view_copyright_policy/', views.domino_view_copyright_policy, name='tfb-domino_view_copyright_policy'),
    path('domino_view_events_information/', views.domino_view_events_information, name='tfb-domino_view_events_information'),
    path('domino_view_guest_control/', views.domino_view_guest_control, name='tfb-domino_view_guest_control'),
    path('domino_view_hub_information/', views.domino_view_hub_information, name='tfb-domino_view_hub_information'),
    path('domino_view_manager_login/', views.domino_view_manager_login, name='tfb-domino_view_manager_login'),
  #  path('manager_login/', auth_views.LoginView.as_view(template_name='manager_login.html'), name='tfb-manager_login'),
  #  path('manager_logout/', auth_views.LogoutView_as_view(template_name='manager/manager_profile.html'), name='tfb-manager_logout'),
  
  #  path('domino_view_press/', views.press, name='tfb-press'),
    path('domino_view_privacy_policy/', views.domino_view_privacy_policy, name='tfb-domino_view_privacy_policy'),
    path('domino_view_user_agreement/', views.domino_view_user_agreement, name='tfb-domino_view_user_agreement'),

]