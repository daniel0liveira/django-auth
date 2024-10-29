
from django.urls import path, include

from home import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('', include('home.urls')),
]
