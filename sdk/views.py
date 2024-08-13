from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import Post

from django.http import HttpResponse
from django.shortcuts import get_object_or_404


class BaseController(View):

    pass


class NotifyController(LoginRequiredMixin, View):

    def get(self, request, post_id=None):
        # Handles both index and show actions
        if post_id:
            post = Post.objects.get(pk=post_id)
            return render(request, 'post_detail.html', {'post': post})
        else:
            posts = Post.objects.all()
            return render(request, 'post_list.html', {'posts': posts})

    def post(self, request):
        # Handles store action
        if not request.user.is_authenticated:
            raise PermissionDenied(
                "Only authenticated users can create new posts.")

        title = request.POST.get('title')
        body = request.POST.get('body')

        if not title or not body:
            return render(request, 'post_form.html', {'error': 'Title and body are required.'})

        post = Post.objects.create(author=request.user, title=title, body=body)

        return redirect('posts.show', post_id=post.id)
