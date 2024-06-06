# main/urls.py
from django.urls import path
from .views import home, contact, news_list, news_detail, register, login_view, logout_view, profile, add_news, \
    edit_news, delete_news

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('news/', news_list, name='news_list'),
    path('news/<int:news_id>/', news_detail, name='news_detail'),
    path('news/<int:news_id>/comment/', news_detail, name='add_comment'),
    path('news/add/', add_news, name='add_news'),
    path('news/<int:news_id>/edit/', edit_news, name='edit_news'),
    path('news/<int:news_id>/delete/', delete_news, name='delete_news'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
]
