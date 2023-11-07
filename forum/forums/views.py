from django.shortcuts import render, redirect
from .models import Category, Topic, MyUser
from .forms import TopicForm
def dashboard(request):
    categories = Category.objects.all()
    topics = Topic.objects.all()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user_id = request.user  # Set the user ID for the topic.
            topic.category = Category.objects.get(category_id=request.POST.get('category_id'))  # Set the category for the topic.
            topic.save()
            print(request.POST.get('category_id'))
            return redirect('dashboard')  # Redirect to the dashboard after topic creation.
    else:
        form = TopicForm()

    return render(request, 'dashboard.html', {'categories': categories, 'topics': topics, 'form': form})

