
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('newform',views.newform,name='newform'),
    path('form2', views.detailform, name='detailform'),
    path('logout',views.logout,name='logout')


    # path('index.html/',views.index,name='index'),
    # path('index.html/register.html')

]