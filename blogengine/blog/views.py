from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import View

from blog.utils import *

from .models import Post, Tag
from .forms import TagForm, PostForm

from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin



def posts_list(request):
	posts = Post.objects.all()
	paginator = Paginator(posts,2)
	page_number = request.GET.get('page',1)
	page = paginator.get_page(page_number)
	is_paginated=page.has_other_pages()
	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url=''
	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url=''
	context = {
		'page':page,
		'is_paginated': is_paginated,
		'next_url':next_url,
		'prev_url':prev_url
	}

	return render(request, 'blog/index.html', context=context)

class PostCreate(LoginRequiredMixin,ObjectCreateMixin,View):
	model_form = PostForm
	template = 'blog/post_create.html'
	raise_exception = True

class PostDetail(ObjectDetailMixin,View):
	model = Post
	template = 'blog/post_detail.html'

class PostUpdate(LoginRequiredMixin,ObjectUpdateMixin, View):
	model = Post
	model_form = PostForm
	template = 'blog/post_update.html'
	raise_exception = True

class PostDelete(LoginRequiredMixin,ObjectDeleteMixin, View):
	model = Post
	template = 'blog/post_delete.html'
	redirect_url = 'posts_list_url'
	raise_exception = True



def tags_list(request):
	tags=Tag.objects.all()
	return render(request,'blog/tags_list.html', context={'tags': tags})

class TagDetail(ObjectDetailMixin,View):
	model = Tag
	template = 'blog/tag_detail.html'

class TagCreate(LoginRequiredMixin,ObjectCreateMixin,View):
	model_form = TagForm
	template = 'blog/tag_create.html'
	raise_exception = True

class TagUpdate(LoginRequiredMixin,ObjectUpdateMixin,View):
	model = Tag
	model_form = TagForm
	template = 'blog/tag_update.html'
	raise_exception = True

class TagDelete(LoginRequiredMixin,ObjectDeleteMixin, View):
	model=Tag
	template='blog/tag_delete.html'
	rediect_url='tags_list_url'
	raise_exception = True
