from django.db import models

# Create your models here.
class Post(models.Model):
    text_content = models.CharField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    likes = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='post_images')

