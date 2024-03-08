from django.urls import path
from .import views
from django.contrib.auth.views import LoginView

urlpatterns=[
    path('',views.index,name="index"),
    path('index/',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('login/',LoginView.as_view(template_name='login.html'),name="login"),
    path('afterlogin',views.afterlogin_view,name="afterlogin"),
    path('userpage/',views.userpage,name="userpage"),
    path('profile/',views.profile,name="profile"),
    path('logout/',views.logout_request,name="logout"),
    path('tts/',views.tts,name="tts"),
   
    ]