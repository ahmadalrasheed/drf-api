from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    auther = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    body = models.TextField()

    # to save the time in which the object in the model was created
    created_at = models.DateTimeField(auto_now_add= True)
    # ro save the time in which the object in the model was updated
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title
