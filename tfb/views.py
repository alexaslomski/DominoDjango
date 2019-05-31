from django.shortcuts import render

# Functions for loading each html page within techforbiotech app

def home(request):
    return render(request, 'techforbiotech/home.html')

def domino_view_become_leader(request):
    return render(request, 'techforbiotech/domino_view_become_leader.html', {'title': 'Become Leader'})

def domino_view_get_the_emblem(request):
    return render(request, 'techforbiotech/domino_view_get_the_emblem.html', {'title': 'Get the Emblem'})    

def domino_view_community_guidelines(request):
    return render(request, 'techforbiotech/domino_view_community_guidelines.html', {'title': 'Community Guidelines'})

def domino_view_contact(request):
    return render(request, 'techforbiotech/domino_view_contact.html', {'title': 'Contact'})

def domino_view_cookie_policy(request):
    return render(request, 'techforbiotech/domino_view_cookie_policy.html', {'title': 'Cookie Policy'})

def domino_view_copyright_policy(request):
    return render(request, 'techforbiotech/domino_view_copyright_policy.html', {'title': 'Copyright Policy'})

def domino_view_events_information(request):
    return render(request, 'techforbiotech/domino_view_events_information.html', {'title': 'Events Information'})    

def domino_view_guest_control(request):
    return render(request, 'techforbiotech/domino_view_guest_control.html', {'title': 'Guest Control'})

def domino_view_hub_information(request):
    return render(request, 'techforbiotech/domino_view_hub_information.html', {'title': 'Hub Information'})

def domino_view_manager_login(request):
    return render(request, 'techforbiotech/domino_view_manager_login.html', {'title': 'Manager Login'})     

 

def domino_view_privacy_policy(request):
    return render(request, 'techforbiotech/domino_view_privacy_policy.html', {'title': 'Privacy Policy'})

def domino_view_user_agreement(request):
    return render(request, 'techforbiotech/domino_view_user_agreement.html', {'title': 'User Agreement'})    


