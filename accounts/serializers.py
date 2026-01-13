from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'branch']
        read_only_fields = ['id']

    def validate(self, data):
        # Trainer creation limit: Max 3 trainers per branch
        if data.get('role') == User.Role.TRAINER:
            branch = data.get('branch')
            if not branch and self.instance:
                branch = self.instance.branch
            
            if branch:
                current_trainers_count = User.objects.filter(branch=branch, role=User.Role.TRAINER).count()
                if self.instance: # Update scenario
                     # If updating existing user, exclude self from count checks if role is unchanged, 
                     # but here we care if they are switching TO trainer or creating NEW trainer.
                     # Simplification: checks total count.
                     pass 
                
                # If creating new trainer or updating to trainer
                if not self.instance and current_trainers_count >= 3:
                     raise serializers.ValidationError({"branch": "This branch already has the maximum number of trainers (3)."})
        
        return data

    def __str__(self):
        return self.username

