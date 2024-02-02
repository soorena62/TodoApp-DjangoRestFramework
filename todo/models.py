from django.db import models
from django.contrib.auth import get_user_model
# Create your models here:

User = get_user_model()


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    name = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField(default=1)
    done = models.BooleanField(default=False)

    class Meta:
        db_table = 'todos'
