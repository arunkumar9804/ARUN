from django.urls import path
from . import views
urlpatterns = [

    path('',views.index,name="home_page"),
    path('samp/',views.samp,name="comment_entry"),
    path('login/',views.login,name="login_page"),
    path('register/',views.register,name="register_page"),
    path('logout/',views.logout,name="logout"),
    
]