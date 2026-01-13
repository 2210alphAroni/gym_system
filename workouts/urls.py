from django.urls import path
from .views import WorkoutPlanListCreateView

urlpatterns = [
    path('plans/', WorkoutPlanListCreateView.as_view(), name='workout-plan-list-create'),
]
