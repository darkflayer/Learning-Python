from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CommentForm
from .models import Comment,BlogPost


def post_list(request):
    posts = BlogPost.objects.filter(author=request.user)  # Show only user's posts
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        BlogPost.objects.create(title=title, content=content, author=request.user)
        return redirect('post_list')
    return render(request, 'blog/post_form.html')

@login_required
def post_update(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post_list')
    return render(request, 'blog/post_form.html', {'post': post})

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    post.delete()
    return redirect('post_list')



def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_list')
        else:
            return render(request, "blog/login.html", {"error": "Invalid credentials"})
    return render(request, "blog/login.html")

def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            return render(request, "blog/register.html", {"error": "Passwords do not match"})

        if User.objects.filter(username=username).exists():
            return render(request, "blog/register.html", {"error": "Username already taken"})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("post_list")

    return render(request, "blog/register.html")

def post_details(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    comments = post.comments.all()  # Fetch comments for this post
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_post = post  # Link the comment to the correct blog post
            comment.author = request.user
            comment.save()
            return redirect("post_details", post_id=post.id)

    return render(request, "blog/post_details.html", {"post": post, "comments": comments, "form": form})