from django.urls import path
from home.views import home, blog_detail, about

urlpatterns = [
    path('', home, name='home'),
    path("post/<str:slug>/", blog_detail, name="post-detail"),
    path("profile/", about, name="about")
]
