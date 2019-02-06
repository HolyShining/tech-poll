from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('<int:department_id>', csrf_exempt(views.AnswersView.as_view()), name='answers'),
]