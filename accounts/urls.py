from django.urls import path
from .views import UserProfileView, UserListCreateView

urlpatterns = [
    path('me/', UserProfileView.as_view(), name='user-profile'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
]
