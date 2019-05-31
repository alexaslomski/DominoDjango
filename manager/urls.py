from django.urls import path
from . import views

urlpatterns = [
    path('manager_view_my_profile/', views.manager_view_my_profile, name='manager-manager_view_my_profile'),
    path('manager_view_see_discounted_restaurants_and_bars/', views.manager_view_see_discounted_restaurants_and_bars, name='manager-manager_view_see_discounted_restaurants_and_bars'),
    path('manager_view_events_details/', views.manager_view_events_details, name='manager-manager_view_events_details'),
    path('manager_view_list_of_attendees/', views.manager_view_list_of_attendees, name='manager-manager_view_list_of_attendees'),
    path('manager_view_list_of_interested/', views.manager_view_list_of_interested, name='manager-manager_view_list_of_interested'),
    path('manager_view_list_of_cant_attend/', views.manager_view_list_of_cant_attend, name='manager-manager_view_list_of_cant_attend'),
]