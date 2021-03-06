from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('add', views.add , name='add'),
    path('insert', views.insert , name='insert'),
    path('about', views.about , name='about'),
    path('update/<int:id>', views.update , name='update'),
    path('delete/<int:id>', views.delete , name='delete'),

    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('signup',views.signup, name='signup'),
    path('profile',views.profile, name='profile'),
    # path('one', views.addshow, name='addshow'),
    # path('account/register/',views.register, name='register')
    
]