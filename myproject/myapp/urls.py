from django.urls import path,include

from django.urls import re_path

from . import views

# handler404 = 'myapp.views.notfound'




urlpatterns = [
    path('',views.index,name='index'),
    path('counter',views.counter,name='counter'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('post/<str:pk>',views.post,name='post'),  
    re_path(r'^.*$',views.page404),
]
