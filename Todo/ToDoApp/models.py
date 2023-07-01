from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=400, null=False)
    date = models.DateField(null=False, blank=True)

    def __str__(self) -> str:
        return self.id