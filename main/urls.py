from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pooja/', views.pooja_list, name='pooja'),
    path('book/<int:id>/', views.book_pooja, name='book'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin-portal/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-portal/temples/', views.manage_temples, name='manage_temples'),
    path('admin-portal/temples/edit/<int:id>/', views.edit_temple, name='edit_temple'),
    path('admin-portal/temples/delete/<int:id>/', views.delete_temple, name='delete_temple'),
    path('admin-portal/poojas/', views.manage_poojas, name='manage_poojas'),
    path('admin-portal/poojas/edit/<int:id>/', views.edit_pooja, name='edit_pooja'),
    path('admin-portal/poojas/delete/<int:id>/', views.delete_pooja, name='delete_pooja'),
    path('payment/<int:booking_id>/', views.payment_selection, name='payment_selection'),
    path('payment/process/<int:booking_id>/', views.process_payment, name='process_payment'),
    path('payment/success/<int:booking_id>/', views.payment_success, name='payment_success'),
]