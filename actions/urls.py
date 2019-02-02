from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('sections/', views.SectionView.as_view(), name='create-section'),
    path('stage/', views.StageView.as_view(), name='create-stage'),
    path('question/', views.QuestionView.as_view(), name='create-question'),
]
