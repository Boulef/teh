from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import TV

class TVListView(ListView):
    model = TV
    template_name = 'tv_list.html'  # Replace with the actual template name
    context_object_name = 'tv_list'  # Replace with the desired context variable name

    def get_queryset(self):
        # You can customize the queryset if needed
        return TV.objects.all()