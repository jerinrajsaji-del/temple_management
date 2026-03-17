from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pooja/', views.pooja_list, name='pooja'),
    path('book/<int:id>/', views.book_pooja, name='book'),
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
   
]