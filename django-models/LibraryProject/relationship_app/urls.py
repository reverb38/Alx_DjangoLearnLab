from django.urls import path
from . import views

urlpatterns = [
    # Function-based view
    path('books/', views.list_books, name='list_books'),

    # Class-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

from django.urls import path
from .views import login_view, logout_view, register_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]

