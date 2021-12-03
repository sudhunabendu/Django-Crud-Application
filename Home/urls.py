from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('add', views.add , name='add'),
    path('insert', views.insert , name='insert'),
    path('about', views.about , name='about'),
    path('update/<int:id>', views.update , name='update'),
    path('delete/<int:id>', views.delete , name='delete'),
    # path('accounts/', include('accounts.urls')),
    # path('account/register/',views.register, name='register')
    
]