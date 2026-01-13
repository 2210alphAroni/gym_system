from rest_framework import generics, permissions
from .models import Branch
from .serializers import BranchSerializer
from accounts.permissions import IsSuperAdmin

class BranchListCreateView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]
