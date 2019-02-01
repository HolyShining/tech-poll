from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', views.AdminView.as_view(), name='admin-dashboard'),
    path('user/', views.UserView.as_view(), name='user-dashboard'),
    path('', include('actions.urls'))
]