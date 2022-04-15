from django.db import models

# Create your models here.
class Task(models.Model):
    # Django auto-create a primary-key ID field
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description

class Note(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
