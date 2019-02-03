from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllUsersView.as_view(), name='all-users'),
    path('<int:user_id>', views.UserDetail.as_view(), name='user-details'),
    path('createuser/', views.SignUpView.as_view(), name='create-user'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('routing/', views.Routing.as_view(), name='auth-routing')
]