from App_Login import views
from django.urls import path

from . import views

app_name = 'App_Login'


urlpatterns = [

    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('changeprofile/', views.user_change, name='changeprofile'),
    path('password/', views.pass_change, name='userchange'),
    path('add-picture/', views.add_pro_pic, name='add_pro_pic'),

]
