from django.contrib import admin
from .models import Post, Tag, Image, Video, Me, Ability

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Video)

admin.site.register(Me)
admin.site.register(Ability)