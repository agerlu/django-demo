from django.urls import include

from. import views

from django.conf.urls import  url

urlpatterns = [
    url('index/',views.index),
    url('login/',views.login),
    url('register/',views.register),
    url('logout/',views.logout),
    url('captcha',include('captcha.urls'))
]