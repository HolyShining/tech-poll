from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnswersView.as_view(), name='answers'),
]