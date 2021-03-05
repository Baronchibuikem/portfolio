from django.shortcuts import render
from home.forms import BlogForm, SubscriptionForm
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from home.models import Blog, Subscription


def home(request):
    blogs = Blog.objects.filter(status="published").order_by("-created")
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    template = 'blog-list.html'
    context = {
        'posts': page_obj,
    }
    if request.method == 'POST':
        form = SubscriptionForm(request.POST or None,
                                request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Thank you for subscribing")
    else:
        form = SubscriptionForm
    template = 'index.html'
    context = {'subscribe_form': form,  'posts': page_obj, }
    return render(request, template, context)


def blog_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    context = {"post": post}
    template = "blog-detail.html"
    return render(request, template, context)


def about(request):
    template = "about.html"
    return render(request, template, {})
