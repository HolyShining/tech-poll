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
    path('departments/adduser', views.AddUserToDepartment.as_view(), name='add-user-to-departments'),
    path('departments/new', views.CreateDepartmentsView.as_view(), name='create-department'),
    path('departments/edit/<int:object_id>', views.DepartmentsDetailView.as_view(), name='edit-department'),
    path('load/sections', views.SectionLoadFile.as_view(), name='load-sections-file'),
    path('load/stages', views.StageLoadFile.as_view(), name='load-stage-file'),
    path('load/questions', views.QuestionLoadFile.as_view(), name='load-question-file'),
    path('grades/', views.GradesView.as_view(), name='grades'),
    path('grade/new', views.CreateGradeView.as_view(), name='create-grade-view'),
    path('grade/edit/<int:object_id>', views.GradeDetailView.as_view(), name='edit-grade'),
]
