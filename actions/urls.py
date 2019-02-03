from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    # path('sections/', views.CreateSectionView.as_view(), name='create-section'),
    path('sections/new', views.CreateSectionView.as_view(), name='create-section'),
    path('stage/new', views.CreateStageView.as_view(), name='create-stage'),
    path('question/new', views.CreateQuestionView.as_view(), name='create-question'),
    path('departments/new', views.CreateDepartmentsView.as_view(), name='create-department'),
    path('load/<mode>', views.LoadFileView.as_view(), name='load-file')
]
