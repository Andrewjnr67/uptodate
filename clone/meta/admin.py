from django.contrib import admin
from . models import Post, BlogCategory, TeamMember, Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "content", "image")
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(BlogCategory)
admin.site.register(TeamMember)
admin.site.register(Comment)
