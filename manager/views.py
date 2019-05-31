from django.shortcuts import render

# Functions for loading each html page within techforbiotech app

def manager_view_my_profile(request):
    return render(request, 'techforbiotech/manager_view_my_profile.html')

def manager_view_see_discounted_restaurants_and_bars(request):
    return render(request, 'techforbiotech/manager_view_see_discounted_restaurants_and_bars.html', {'title': 'See Discounted Restaurants and Bars'})      

def manager_view_events_details(request):
    return render(request, 'techforbiotech/manager_view_events_details.html', {'title': 'Events Details'})   

def manager_view_list_of_attendees(request):
    return render(request, 'techforbiotech/manager_view_list_of_attendees.html', {'title': 'List of Attendees'})  

def manager_view_list_of_interested(request):
    return render(request, 'techforbiotech/manager_view_list_of_interested.html', {'title': 'List of Interested'})  

def manager_view_list_of_cant_attend(request):
    return render(request, 'techforbiotech/manager_view_list_of_cant_attend.html', {'title': 'Cant Attend'})      

  