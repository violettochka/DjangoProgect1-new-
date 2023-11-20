from django.http import HttpResponse
from django.shortcuts import render

menu = [
    {'title': 'login', 'url_name': 'login'},
    {'title': 'registration', 'url_name': 'registration'},
    {'title': 'main_page', 'url_name': 'main'},
    {'title': 'details', 'url_name': 'details'},
    {'title': 'create_new_blog', 'url_name': 'new-blog'}
]


def main(request):
    return render(request, 'myappAccount/main_page.html', {'menu': menu})

def about(request):
    return render(request, 'myappAccount/details.html', {'menu': menu})

def profile(reguest, username):
    return HttpResponse(f'Hey, {username}, it is your own page on the site')

def new_blog(request):
    return render(request, 'myappAccount/new_blog.html', {'menu': menu})

def set_password(request):
    return HttpResponse('Change your personal accounting data')

def set_userdata(request):
    return HttpResponse('Change your personal data')

def deactivate(request):
    return HttpResponse('Deactivate your personal data')

def registration(request):
    return render(request, 'myappAccount/registration.html', {'menu': menu})

def login(request):
    return render(request, 'myappAccount/login.html', {'menu': menu})

def logout(request):
    return HttpResponse('Page for logout')