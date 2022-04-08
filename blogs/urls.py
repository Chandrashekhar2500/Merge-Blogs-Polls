from django.urls import path

from . import views 
app_name = 'blogs' 


urlpatterns = [
    path('post/ <slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('category/ <slug:slug>/', views.category_detail, name='category_detail'),
    path('post/ <slug:slug>/', views.post_detail, name='post_detail'),
    path('tag/ <slug:slug>/', views.tag_detail, name='tag_detail'),
    path('signup_page/', views.signup_page, name='signup_page'),
    path('login_page/', views.login_page, name='login_page'),
    path('logout_page/', views.logout_page, name='logout_page'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('user_update/', views.user_update, name='user_update'),
    path('category_list/', views.category_list, name='category_list'),
    path('tag_list/', views.tag_list, name='tag_list'),

    path('', views.post_list, name='post_list'),


]   