from django.db.models import fields
from django.forms import ModelForm
from .models import Post, PostImage, Comment

class CreatePostForm(ModelForm):
    class Meta:
        exclude=('author', 'likes', 'created_date')
        model = Post

    def save(self, user):
        post = Post.objects.create(
            title = self.cleaned_data['title'],
            text_content = self.cleaned_data['text_content'],
            author = user,
        )
        return post

class AddImageForm(ModelForm):
    class Meta:
        exclude = ('post',)
        model = PostImage
    
    def save(self, post):
        if self.cleaned_data['image']:
            postImage = PostImage.objects.create(
                post = post,
                image = self.cleaned_data['image']
            )
            return postImage

class AddCommentForm(ModelForm):
    class Meta:
        fields = ('comment',)
        model = Comment

    def save(self, post, user):
        comment = Comment.objects.create(
            commentor = user,
            post = post,
            comment = self.cleaned_data['comment']
        )
        return comment