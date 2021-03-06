from django.db import models
from user_app.models import UserModel

# Create your models here.

class PhotoModel(models.Model):
     photo = models.ImageField(upload_to='upload_pic')
     caption = models.TextField(blank=True,null=True)
     timestamp= models.DateTimeField(auto_now_add=True)
     upload_by= models.ForeignKey(UserModel,on_delete=models.CASCADE, related_name='uploaded_post')
     likes=models.PositiveIntegerField(default=0)

class CommentModel(models.Model):
    comment=models.TextField()
    timestamp= models.DateTimeField(auto_now_add=True)
    commented_by=models.ForeignKey(UserModel,on_delete=models.CASCADE, related_name='comments')
    parent_post=models.ForeignKey(PhotoModel,on_delete=models.CASCADE, related_name='comments')

