from django.db import models
from users.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, default=None)
    text_content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    likes = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def like_post(self):
        self.likes += 1
        self.save()
    
    def dislike_post(self):
        self.likes -= 1
        self.save()

    class Meta:
        ordering = ['-created_date']
        
    
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='post_images', blank=True)

class PostLike(models.Model):
    liked_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="liked_post")
    liker_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_liker")
    liked = models.BooleanField(default=False)

    def is_liked(self):
        self.liked = True
        self.save()

    def not_liked(self):
        self.liked = False
        self.save()

class Comment(models.Model):
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentor")
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")

    def like_comment(self):
        self.likes += 1
        self.save()

    def dislike_comment(self):
        self.likes -= 1
        self.save()

    class Meta:
        ordering = ['-created_date']

class CommentLike(models.Model):
    liked_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="liked_comment")
    liker_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_liker")
    liked = models.BooleanField(default=False)

    def is_liked(self):
        self.liked = True
        self.save()

    def not_liked(self):
        self.liked = False
        self.save()