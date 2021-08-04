from django.urls import path
from . import views
app_name = 'App_Blog'


urlpatterns = [

    path('', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='write'),
    path('details/<slug:slug>', views.blog_details, name="blog_details"),
    path('liked/<int:pk>', views.liked, name="liked"),
    path('unliked/<int:pk>', views.unliked, name="unliked"),
    path('myblog/', views.MyBlogs.as_view(), name="myblog"),
    path('edit/<pk>', views.UpdateBlog.as_view(), name="edit_blog")



]
