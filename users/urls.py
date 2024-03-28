from django.urls import path
from .views import LoginView, RegisterView, ListView, DetailView, SettingsView, LogOut, DeleteView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', ListView.as_view(), name='users'),
    path('<int:id>/', DetailView.as_view(), name='user-detail'),
    path('logout/', LogOut.as_view(), name='logout'),
    path('users_delete/<int:id>/', DeleteView.as_view(), name='delete-user'),
    path('settings/<int:id>/', SettingsView.as_view(), name="settings"),
]
