from django.db import models
import uuid
# Create your models here.

class Contact(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    first_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    choice
    theme = models.CharField(max_length=100)
    text = models.CharField(max_length=100)