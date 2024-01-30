from django.db import models

# Create your models here:


class Todo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField(default=1)
    done = models.BooleanField(default=False)

    class Meta:
        db_table = 'todos'
