from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    entries_qs = Post.objects.order_by("date")
    featured = entries_qs.first()
    entries = entries_qs[1:7]  # or paginate this instead

    return render(request, "posts/home.html", {
        "featured": featured,
        "entries": entries,
        "now_learning": ["network security fundamentals", "a side project in Python"],
        "site_name": "Field Notes",
    })

def get_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return HttpResponse(f"Post id {post_id}, title={post.title}")