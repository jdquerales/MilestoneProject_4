from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('title', 'content', 'user', 'created')
    list_filter = ['create', 'user']
    search_fields = ['title']


# Register your models here.
admin.site.register(Review)
