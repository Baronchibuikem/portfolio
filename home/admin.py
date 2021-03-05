from django.contrib import admin
from home.models import Blog, Subscription


class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Subscription)
