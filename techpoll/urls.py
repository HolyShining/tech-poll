from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
    path('api/', include('api.urls')),
    path('users/', include('authentication.urls')),
    path('dash/', include('dashboards.urls')),
    path('answers/', include('answers.urls')),
]
