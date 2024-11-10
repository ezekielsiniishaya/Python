# myapp/urls.py
from django.urls import path
from . import views


# all url paths
urlpatterns = [
    path('csrf/', views.csrf, name='csrf'),
    path('', views.home, name='home'),
    path('book_list/', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('json_view/', views.json_view, name='json_view'),
    path('http_response/', views.http_response, name='HttpResponse'),
    path('create_user/', views.creat_user, name='create_user'),
    path('user_profile/', views.user_profile, name='user_profile'),
]
