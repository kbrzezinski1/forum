from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path('category/<int:category_id>/', views.category_topics, name='category_topics'),
    path('topic/<int:topic_id>/', views.topics, name='topics'),
    path('posts/<int:post_id>/clear_content/', views.delete_post, name='delete_post'),

]