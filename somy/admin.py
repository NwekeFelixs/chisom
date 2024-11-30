from django.contrib import admin

# Register your models here.
from .models import User, Comment, Blog, Category, Like,  SubCategory, Tag, NewsletterSubscription

admin.site.register(User)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'subcategory', 'created', 'published']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['category', 'subcategory', 'tags', 'published']

    # Show subcategory and tags in the admin form
    filter_horizontal = ('tags',)
@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at') 

admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Tag)