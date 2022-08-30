from django.urls import path
from . import views
urlpatterns = [

    path('',views.index,name="home_page"),
    path('samp/',views.samp),
    path('login/',views.login,name="login_page"),
    path('register/',views.register,name="register_page"),
]