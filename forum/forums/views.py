from django.shortcuts import render, redirect
from .models import Category, Topic, MyUser, Post
from .forms import TopicForm, PostForm
from django.core.paginator import Paginator
from django.db.models import F, Max, OuterRef, Subquery
from django.db.models.functions import Coalesce
from django.db.models import Case, When, Value

CONST_POST_PER_PAGE = 20
CONST_TOPIC_PER_PAGE = 10
def dashboard(request):
    categories = Category.objects.all()
    topics = Topic.objects.all()
    return render(request, 'dashboard.html', {'categories': categories, 'topics': topics})

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
    return render(request, 'category_topics.html', {'category': category, 'topics': page, 'form': form})

def topics(request, topic_id):
    topic = Topic.objects.get(topic_id=topic_id)
    posts = Post.objects.filter(topic_id=topic)
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
            return redirect('topics', topic_id=topic_id) 
    else:
        form = PostForm()    
    return render(request, 'topics.html', {'topic': topic, 'posts': page, 'form': form})
