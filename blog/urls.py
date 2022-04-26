from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_page, name='signup'),
    path('post/<int:post_id>/', views.post_page, name='post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete'),
    path('edit/<int:post_id>/', views.edit_post, name='edit'),    
]