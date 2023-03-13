from django.db import models
import uuid
# Create your models here.

class Contact(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    first_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    choice = models.CharField(max_length=100, blank=True)
    theme = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(blank=True, auto_now_add=True)


    def __str__(self) -> str:
        return self.email
