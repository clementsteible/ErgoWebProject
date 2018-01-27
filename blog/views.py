from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.

def post_list(request):
    tri_creations_recentes = Post.objects.filter(published_date__lte=timezone.now()).order_by("created_date")
    return render(request, 'blog/post_list.html', {"tri_creations_recentes" : tri_creations_recentes})
