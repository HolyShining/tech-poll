from django.urls import path
from . import views

urlpatterns = [
    path('createuser/', views.SignUpView.as_view(), name='sign-up')
]