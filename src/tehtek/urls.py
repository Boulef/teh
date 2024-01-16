from django.urls import path
from .views import TVListView

urlpatterns = [
    path('tvs/', TVListView.as_view(), name='tv-list'),
    # Add other URL patterns as needed
]