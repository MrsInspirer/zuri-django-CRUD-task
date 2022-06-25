from django.contrib import admin
from .models import Post
from .models import title
from .models import slug
from .models import author
from .models import body
from .models import publish
from .models import created
from .models import updated
from .models import status

# Register your models here.

admin.site.register(Post)
admin.site.register(title)
admin.site.register(slug)
admin.site.register(author)
admin.site.register(body)
admin.site.register(publish)
admin.site.register(created)
admin.site.register(updated)
admin.site.register(status)


