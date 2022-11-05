from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from core.models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

def listing(request):
    data = {
        "blogs": Blog.objects.all(),
    }
    return render(request, "listing.html", data)

def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    data = {
        "blog": blog,
    }
    return render(request, "view_blog.html", data)

def see_request(request):
    text = f"""
        Some attributes of the HttpRequest object:
        scheme: {request.scheme}
        path: {request.path}
        method: {request.method}
        GET: {request.GET}
        user: {request.user}
    """
    return HttpResponse(text, content_type="text/plain")


def user_info(request):
    text = f"""
        Selected HttpRequest.user attributes:
        username: {request.user.username}
        is_anonymous: {request.user.is_anonymous}
        is_staff: {request.user.is_staff}
        is_superuser: {request.user.is_superuser}
        is_active: {request.user.is_active}
    """
    return HttpResponse(text, content_type="text/plain")

def index(request):
    # ...
    num_authors = Author.objects.count() # The 'all()' is implied by default.
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

@login_required
def private_place(request):
    return HttpResponse("members only!", content_type="text/plain")

@user_passes_test(lambda user: user.is_staff)
def staff_place(request):
    return HttpResponse("Employees Only", content_type="text/plain")

@login_required
def add_messages(request):
    username = request.user.username
    messages.add_message(request, messages.INFO, f"Hello {username}")
    messages.add_message(request, messages.WARNING, "DANGER")
    return HttpResponse("Messages added", content_type="text/plain")

def function(input, output):
    if len(input)==0:
        return []
    for i in range(input[0],input[-1]):
        if i not in input:
            output.append(i)
    return output
