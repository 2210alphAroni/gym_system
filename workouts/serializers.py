from rest_framework import serializers
from .models import WorkoutPlan

class WorkoutPlanSerializer(serializers.ModelSerializer):
    trainer_name = serializers.ReadOnlyField(source='trainer.username')
    branch_name = serializers.ReadOnlyField(source='branch.name')

    class Meta:
        model = WorkoutPlan
        fields = ['id', 'title', 'description', 'trainer', 'trainer_name', 'branch', 'branch_name', 'created_at']
        read_only_fields = ['id', 'trainer', 'branch', 'created_at']
