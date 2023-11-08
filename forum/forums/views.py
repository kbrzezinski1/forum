from django.shortcuts import render, redirect
from .models import Category, Topic, MyUser, Post
from .forms import TopicForm, PostForm
def dashboard(request):
    categories = Category.objects.all()
    topics = Topic.objects.all()
    return render(request, 'dashboard.html', {'categories': categories, 'topics': topics})

def category_topics(request, category_id):
    category = Category.objects.get(category_id=category_id)
    topics = Topic.objects.filter(category_id=category)
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
    return render(request, 'category_topics.html', {'category': category, 'topics': topics, 'form': form})

def topics(request, topic_id):
    topic = Topic.objects.get(topic_id=topic_id)
    posts = Post.objects.filter(topic_id=topic)
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
    return render(request, 'topics.html', {'topic': topic, 'posts': posts, 'form': form})
