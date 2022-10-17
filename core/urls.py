from django import views
from django.urls import path
from. import views
from .apiview import ProfileDetails,PostDetails
urlpatterns=[
    path('',views.index, name="index"),
    path('signup',views.signup, name="signup"),
    path('follow',views.follow, name="follow"),
    path('search',views.search, name="search"),
    path('signin',views.signin, name="signin"),
    path('logout',views.logout, name="logout"),
    path('setting',views.setting, name="setting"),
    path('upload',views.upload, name="upload"),
    path('like-post', views.like_post, name='like-post'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('profile/', ProfileDetails.as_view(),name="profile_list"),
    path('posts/', PostDetails.as_view(), name='posts'),
    




    



]