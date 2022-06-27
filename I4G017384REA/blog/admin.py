from django.contrib import admin

from .models import status, updated, created, publish, body, author, slug, title,Post, 

admin.site.register(Post)
admin.site.register(title)
admin.site.register(slug)
admin.site.register(author)
admin.site.register(body)
admin.site.register(publish)
admin.site.register(created)
admin.site.register(updated)
admin.site.register(status)


