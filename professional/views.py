from django.shortcuts import render

# Functions for loading each html page within techforbiotech app

def pro_view_create_event(request):
    return render(request, 'techforbiotech/pro_view_create_event.html', {'title': 'Create Event'})

def pro_view_edit_your_events(request):
    return render(request, 'techforbiotech/pro_view_edit_your_events.html', {'title': 'Edit Your Events'})

def pro_view_see_your_coming_events(request):
    return render(request, 'techforbiotech/pro_view_see_your_coming_events.html', {'title': 'See Your Coming Events'})      

def pro_view_events_details(request):
    return render(request, 'techforbiotech/pro_view_events_details.html', {'title': 'Events Details'})   

def pro_view_event_space_details(request):
    return render(request, 'techforbiotech/pro_view_event_space_details.html', {'title': 'Event Space Details'})   
     
def pro_view_see_discounted_restaurants_and_bars(request):
    return render(request, 'techforbiotech/pro_view_see_discounted_restaurants_and_bars.html', {'title': 'Discounted Restaurants and Bars'})     

def pro_view_hubspot(request):
    return render(request, 'techforbiotech/pro_view_hubspot.html', {'title': 'Hubspot'})

def pro_view_my_profile(request):
    return render(request, 'techforbiotech/pro_view_my_profile.html', {'title': 'My Profile'})

def pro_view_list_of_attendees(request):
    return render(request, 'techforbiotech/pro_view_list_of_attendees.html', {'title': 'List of Attendees'})

def pro_view_list_of_interested(request):
    return render(request, 'techforbiotech/pro_view_list_of_interested.html', {'title': 'List of Interested'})

def pro_view_list_of_cant_attend(request):
    return render(request, 'techforbiotech/pro_view_list_of_cant_attend.html', {'title': 'List of Cant Attend'})

def pro_view_edit_events_list_of_attendees(request):
    return render(request, 'techforbiotech/pro_view_edit_events_list_of_attendees.html', {'title': 'List of Attendees'})

def pro_view_edit_events_list_of_interested(request):
    return render(request, 'techforbiotech/pro_view_edit_events_list_of_interested.html', {'title': 'List of Interested'})

def pro_view_edit_events_list_of_cant_attend(request):
    return render(request, 'techforbiotech/pro_view_edit_events_list_of_cant_attend.html', {'title': 'List of Cant Attend'})

def pro_view_buy_tickets(request):    
    return render(request, 'techforbiotech/pro_view_buy_tickets.html', {'title': 'List of Cant Attend'})    