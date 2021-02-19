from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, PostImage, Comment, PostLike, CommentLike
from .forms import CreatePostForm, AddImageForm, AddCommentForm


# Create your views here.
class PostListView(FormView, TemplateView):
    model = Post
    template_name = "forum/post_list.html"
    form_class = CreatePostForm

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        if self.kwargs['filter'] == "latest":
            posts = Post.objects.all()
            context['filter_type'] = "latest"
        elif self.kwargs['filter'] == "popular":
            posts = Post.objects.order_by('-likes')
            context['filter_type'] = "popular"
        
        context['posts'] = posts

        if 'create_post_form' not in context:
            context['create_post_form'] = CreatePostForm()
        
        if 'add_image_form' not in context:
            context['add_image_form'] = AddImageForm()

        return context

    def post(self, request, *args, **kwargs):
        
        context = {}

        if 'create_post' in request.POST:
            create_post_form = CreatePostForm(request.POST)
            add_image_form = AddImageForm(request.POST, request.FILES)

            if create_post_form.is_valid() and add_image_form.is_valid():
                post = create_post_form.save(self.request.user)
                add_image_form.save(post)
            else:
                context['create_post_form'] = create_post_form

        return render(request, self.template_name, self.get_context_data(**context))


class PostDetailView(FormView, DetailView, LoginRequiredMixin):
    model = Post
    form_class = CreatePostForm
    template_name = 'forum/post_detail.html'

    def get_context_data(self, **kwargs):
        post = Post.objects.filter(pk=self.kwargs['pk']).first()
        comments = Comment.objects.filter(post = post)

        post_image = PostImage.objects.filter(post = post)
        liked_post = PostLike.objects.filter(liked_post=self.kwargs['pk'], liker_user = self.request.user).first()
        if liked_post != None:
            liked_post = liked_post.liked
        context =  super(PostDetailView, self).get_context_data(**kwargs)
        context['post'] = post
        context['comments'] = comments
        context['post_image'] = post_image
        context['liked_post'] = liked_post

        if 'comment_form' not in context:
            context['comment_form'] = AddCommentForm()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = {}

        current_post = Post.objects.filter(pk=self.kwargs['pk']).first()

        if 'add_comment' in request.POST:
            add_comment_form = AddCommentForm(request.POST)

            if add_comment_form.is_valid():
                add_comment_form.save(current_post, self.request.user)
            else:
                context['comment_form'] = add_comment_form
        
        if 'like_post' in request.POST:
            current_post.like_post()
            liked_post = PostLike.objects.filter(liked_post=current_post, liker_user = self.request.user).first()
            if liked_post == None:
                liked_post = PostLike.objects.create(liked_post=current_post, liker_user = self.request.user)
                liked_post.is_liked()
            else:
                liked_post.is_liked()
            
        
        if 'dislike_post' in request.POST:
            current_post.dislike_post()
            liked_post = PostLike.objects.filter(liked_post=current_post, liker_user = self.request.user).first()
            liked_post.not_liked()
        
        if 'like_comment' in request.POST:
            current_comment = Comment.objects.filter(pk=request.POST['comment_data']).first()
            current_comment.like_comment()
            liked_comment = CommentLike.objects.filter(liked_comment=current_comment, liker_user = self.request.user).first()
            if liked_comment == None:
                liked_comment = CommentLike.objects.create(liked_comment=current_comment, liker_user = self.request.user)
                liked_comment.is_liked()
            else:
                liked_comment.is_liked()

        if 'dislike_comment' in request.POST:
            current_comment = Comment.objects.filter(pk=request.POST['comment_data']).first()
            current_comment.dislike_comment()
            liked_comment = CommentLike.objects.filter(liked_comment=current_comment, liker_user = self.request.user).first()
            liked_comment.not_liked()
        
        return render(request, self.template_name, self.get_context_data(**context))


