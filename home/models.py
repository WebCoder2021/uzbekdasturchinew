from django.db import models
from users.models import CustomUser
# Create your models here.
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question

class Email_send(models.Model):
    email = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.email

class SendMessages(models.Model):
    email = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    message = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email

