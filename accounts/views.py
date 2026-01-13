from rest_framework import generics, permissions
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserListCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == User.Role.SUPER_ADMIN:
            return User.objects.all()
        elif user.role == User.Role.GYM_MANAGER:
            return User.objects.filter(branch=user.branch)
        return User.objects.none() # Others cannot list users

    def perform_create(self, serializer):
        user = self.request.user
        if user.role == User.Role.GYM_MANAGER:
            # Force assignment to Manager's branch
            serializer.save(branch=user.branch)
        else:
            # Super Admin can optionally set branch, or serializer handles it from data
            serializer.save()

class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
