from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('sections/', views.SectionView.as_view(), name='sections'),
    path('sections/new', views.CreateSectionView.as_view(), name='create-section'),
    path('sections/edit/<int:object_id>', views.SectionDetailView.as_view(), name='edit-section'),
    path('stage/', views.StagesView.as_view(), name='stages'),
    path('stage/new', views.CreateStageView.as_view(), name='create-stage'),
    path('stage/edit/<int:object_id>', views.StageDetailView.as_view(), name='edit-stage'),
    path('question/', views.QuestionsView.as_view(), name='questions'),
    path('question/new', views.CreateQuestionView.as_view(), name='create-question'),
    path('question/edit/<int:object_id>', views.QuestionDetailView.as_view(), name='edit-question'),
    path('departments/', views.DepartmentsView.as_view(), name='departments'),
    path('departments/new', views.CreateDepartmentsView.as_view(), name='create-department'),
    path('departments/edit/<int:object_id>', views.DepartmentsDetailView.as_view(), name='edit-department'),
    path('load/<mode>', views.LoadFileView.as_view(), name='load-file')
]
