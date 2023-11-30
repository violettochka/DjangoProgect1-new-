from django.urls import path
from .views import *
urlpatterns = [
    path('profile/<str:username>/', profile),
    path('set-password/', set_password),
    path('set-userdata/', set_userdata),
    path('login/', login, name='login'),
    path('logout/', logout),
    path('registration/', registration, name='registration'),
    path('deactivate/', deactivate),
    path('new-blog/', new_blog, name= 'new-blog'),
    path('', main, name ='main'),
]