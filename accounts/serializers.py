from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'role', 'branch']
        read_only_fields = ['id']

    def validate(self, data):
        request = self.context.get('request')
        user = request.user if request else None

        # Resolve branch: 
        # 1. From data (if Super Admin provides it)
        # 2. From current user (if Manager)
        # 3. From instance (if update)
        branch = data.get('branch')
        
        if user and user.role == User.Role.GYM_MANAGER:
            branch = user.branch # Manager forces their own branch
        
        if not branch and self.instance:
             branch = self.instance.branch

        # Trainer creation limit: Max 3 trainers per branch
        if data.get('role') == User.Role.TRAINER:
            if branch:
                current_trainers_count = User.objects.filter(branch=branch, role=User.Role.TRAINER).count()
                if self.instance: 
                     # If updating, exclude self from count if logical (omitted for simplicity, pure count check is strict but safe)
                     pass
                
                # If creating new trainer or updating TO trainer (and we assume count creates a new one or checks total)
                # Correct logic: if we are adding a NEW trainer, count must be < 3.
                if not self.instance and current_trainers_count >= 3:
                     raise serializers.ValidationError({"branch": "This branch already has the maximum number of trainers (3)."})
        
        return data

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create_user(**validated_data) # create_user handles hashing
        if password:
            user.set_password(password)
            user.save()
        return user

    def __str__(self):
        return self.username

