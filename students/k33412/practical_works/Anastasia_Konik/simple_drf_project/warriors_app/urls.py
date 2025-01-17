from django.urls import path
from .views import *

app_name = "warriors_app"

urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('profession/create/', ProfessionCreateView.as_view()),
    path('skills/', SkillsApiView.as_view()),
    path('skills/create/', SkillsCreateView.as_view()),
    path('warriorprof/', WarriorProfessionView.as_view()),
    path('warriorskill/', WarriorsSkillsView.as_view()),
    path('information/<int:pk>/', AllWarriorsInformation.as_view()),
    path('delete/<int:pk>/', DeleteWarrior.as_view()),
    path('update/<int:pk>/', UpdateWarrior.as_view()),
]
