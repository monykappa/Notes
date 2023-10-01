from django.urls import path
from . import views


app_name = 'userprofile' 
urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.custom_logout, name='custom_logout'),
]
