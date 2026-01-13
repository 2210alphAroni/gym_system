from django.urls import path
from .views import BranchListCreateView

urlpatterns = [
    path('branches/', BranchListCreateView.as_view(), name='branch-list-create'),
]
