from rest_framework import generics, permissions
from .models import WorkoutPlan
from .serializers import WorkoutPlanSerializer
from accounts.models import User
from accounts.permissions import IsGymManager, IsTrainer

class IsTrainerOrManagerReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return request.user.role in [User.Role.GYM_MANAGER, User.Role.TRAINER]
            return request.user.role == User.Role.TRAINER
        return False

class WorkoutPlanListCreateView(generics.ListCreateAPIView):
    serializer_class = WorkoutPlanSerializer
    permission_classes = [permissions.IsAuthenticated, IsTrainerOrManagerReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.role == User.Role.GYM_MANAGER:
            return WorkoutPlan.objects.filter(branch=user.branch)
        elif user.role == User.Role.TRAINER:
            # Trainers see their own plans (or potentially all in branch, opting for own for now)
            return WorkoutPlan.objects.filter(trainer=user)
        return WorkoutPlan.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if user.role == User.Role.TRAINER:
            serializer.save(trainer=user, branch=user.branch)
        else:
             pass
