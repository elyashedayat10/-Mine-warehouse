from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
user = get_user_model()


class UserActivity(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
