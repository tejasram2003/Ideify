from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('post/<str:pk>',views.post,name='post'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('profile/<str:name>',views.profile,name='profile'),
    path('edit/',views.edit,name='edit'),
    path('new',views.new,name='new'),
    path('delete/<str:id>',views.delete,name='delete'),
    path('cancel',views.cancel,name='cancel')
]