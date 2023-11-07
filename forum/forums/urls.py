from django.urls import include, path
from forums.views import dashboard

urlpatterns = [
    path("", dashboard, name="dashboard"),
]