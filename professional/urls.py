from django.urls import path
from . import views


urlpatterns = [
    path('pro_view_create_event/', views.pro_view_create_event, name='professional-pro_view_create_event'),
    path('pro_view_edit_your_events/', views.pro_view_edit_your_events, name='professional-pro_view_edit_your_events'),
    path('pro_view_events_details/', views.pro_view_events_details, name='professional-pro_view_events_details'),
    path('pro_view_event_space_details/', views.pro_view_event_space_details, name='professional-pro_view_event_space_details'),
    path('pro_view_see_your_coming_events/', views.pro_view_see_your_coming_events, name='professional-pro_view_see_your_coming_events'),
    path('pro_view_see_discounted_restaurants_and_bars/', views.pro_view_see_discounted_restaurants_and_bars, name='professional-pro_view_see_discounted_restaurants_and_bars'),
    path('pro_view_hubspot/', views.pro_view_hubspot, name='professional-pro_view_hubspot'),
    path('pro_view_my_profile/', views.pro_view_my_profile, name='professional-pro_view_my_profile'),
    path('pro_view_list_of_attendees/', views.pro_view_list_of_attendees, name='professional-pro_view_list_of_attendees'),
    path('pro_view_list_of_interested/', views.pro_view_list_of_interested, name='professional-pro_view_list_of_interested'),
    path('pro_view_list_of_cant_attend/', views.pro_view_list_of_cant_attend, name='professional-pro_view_list_of_cant_attend'),
    path('pro_view_edit_events_list_of_attendees/', views.pro_view_edit_events_list_of_attendees, name='professional-pro_view_edit_events_list_of_attendees'),
    path('pro_view_edit_events_list_of_interested/', views.pro_view_edit_events_list_of_interested, name='professional-pro_view_edit_events_list_of_interested'),
    path('pro_view_edit_events_list_of_cant_attend/', views.pro_view_edit_events_list_of_cant_attend, name='professional-pro_view_edit_events_list_of_cant_attend'),
    path('pro_view_buy_tickets/', views.pro_view_buy_tickets, name='professional-pro_view_buy_tickets'),
]