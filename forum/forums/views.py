from django.shortcuts import render, redirect
from .models import Category, Topic, Post
from .forms import TopicForm, PostForm
from django.core.paginator import Paginator
from django.db.models import F, Max
from django.db.models.functions import Coalesce
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
CONST_POST_PER_PAGE = 20
CONST_TOPIC_PER_PAGE = 10
def dashboard(request):
    
    categories = Category.objects.all()
    topics = Topic.objects.all()
    
    return render(request, 'forums/dashboard.html', {'categories': categories, 'topics': topics})

def category_topics(request, category_id):
    
    category = Category.objects.get(category_id=category_id)
    topics = Topic.objects.filter(category_id=category_id).annotate(latest_post_date=Coalesce(Max('post__created_at'), F('created_at'))).order_by('-latest_post_date', '-created_at')
    paginator = Paginator(topics, CONST_TOPIC_PER_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    if request.method == 'POST':
        form = TopicForm(request.POST)       
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user_id = request.user
            topic.category_id = category
            topic.save()
            return redirect('category_topics', category_id=category_id) 
    else:
        form = TopicForm()    
           
    return render(request, 'forums/category_topics.html', {'category': category, 'topics': page, 'form': form})

def topics(request, topic_id, post_title=None):
    
    topic = Topic.objects.get(topic_id=topic_id)
    posts = Post.objects.filter(topic_id=topic).order_by('created_at')
    paginator = Paginator(posts, CONST_POST_PER_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    if request.method == 'POST':
        form = PostForm(request.POST)       
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            post.topic_id = topic
            post.save()
            last_page = paginator.num_pages
            last_page_url = reverse('topics', args=[topic_id, post_title])
            last_page_url += f'?page={last_page}'
            return HttpResponseRedirect(last_page_url)
    else:
        form = PostForm()   

    return render(request, 'forums/topics.html', {'topic': topic, 'posts': page, 'form': form})

def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    post.content = None 
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'), '/')
