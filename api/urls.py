from django.urls import path
from api import views

urlpatterns = [
    path('questions/<slug:department>', views.QuestionsAPI.as_view(), name='questions-API'),
    path('answers/<slug:user>', views.UserAnswersAPI.as_view(), name='user-answers-API'),
]