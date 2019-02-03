from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('sections/', views.SectionView.as_view(), name='create-section'),
    path('stage/', views.StageView.as_view(), name='create-stage'),
    path('question/', views.QuestionView.as_view(), name='create-question'),
    path('departments/', views.DepartmentsView.as_view(), name='create-department'),
    path('load/<mode>', views.LoadFileView.as_view(), name='load-file')
]
