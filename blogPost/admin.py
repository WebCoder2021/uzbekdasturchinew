from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(PostTags)
admin.site.register(PostCategory)
admin.site.register(PostLike)
admin.site.register(PostDisLike)
admin.site.register(Comment)
class PostsAdmin(admin.ModelAdmin):
    list_display = ["id","title"]
    list_display_links = ('id',"title")
    prepopulated_fields = {'slug':('title',),}
    save_as = True
    group_fieldsets = True
admin.site.register(Post,PostsAdmin)