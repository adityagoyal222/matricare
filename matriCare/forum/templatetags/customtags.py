from django import template
from forum.models import CommentLike

register = template.Library()


def liked_comment(comment, user):
    liked_comment = CommentLike.objects.filter(liked_comment = comment, liker_user = user).first()
    if liked_comment:
        return liked_comment.liked
    else:
        return False

register.filter('liked_comment', liked_comment)