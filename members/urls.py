from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('members/', views.members, name='members'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('another-page/', views.another_page, name='another_page'),
    path('js_game/', views.js_game, name='js_game'),
    path('products/', views.products, name='products'),
]