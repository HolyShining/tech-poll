from django.urls import path
from api import views

urlpatterns = [
    path('questions/<int:department_id>', views.QuestionsAPI.as_view(), name='questions-API'),
    path('answers/', views.UserAnswersAPI.as_view(), name='user-answers-API'),
]