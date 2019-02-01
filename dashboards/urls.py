from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.AdminView.as_view(), name='admin-dashboard'),
    path('user/', views.UserView.as_view(), name='user-dashboard'),
]