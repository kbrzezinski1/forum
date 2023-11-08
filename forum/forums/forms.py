from .models import Topic, Post
from django.forms import ModelForm, TextInput, EmailInput, Textarea

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'content']
        widgets = {
            'title': TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'content': Textarea(attrs={'class': 'w-full p-2 border rounded'}),
        }

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': Textarea(attrs={'class': 'w-full p-2 border rounded'}),
        }