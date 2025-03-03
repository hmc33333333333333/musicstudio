from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile',views.profile, name="profile"),
    path('login',views.login,name="login"),
    path('register',views.register, name= "register"),
    path('contact/', views.contact, name="contact"),
]
