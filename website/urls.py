from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('generate_room/', views.generate_room, name='generate_room'),
    path('room/<str:room>/', views.room, name='room'),
    path('send/', views.send, name='send'),
    # path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    # path('getResponse/<str:room>/', views.getResponse, name='getResponse'),
    path('display_tickets/', views.display_tickets, name='display_tickets'),
    path('generate_ticket/', views.generate_ticket, name='generate_ticket')
]
