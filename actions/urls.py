from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('sections/', views.SectionView.as_view(), name='create-section')
]
