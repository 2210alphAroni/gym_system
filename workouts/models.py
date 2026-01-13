from django.db import models
from django.conf import settings

class WorkoutPlan(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    trainer = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='workout_plans',
        limit_choices_to={'role': 'TRAINER'}
    )
    branch = models.ForeignKey(
        'gyms.Branch', 
        on_delete=models.CASCADE, 
        related_name='workout_plans'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.trainer.username}"
