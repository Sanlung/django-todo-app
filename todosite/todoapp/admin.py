from django.contrib import admin
from .models import Task, Note, Comment, Tag

# Register your models here.
admin.site.register(Task)
admin.site.register(Note)
admin.site.register(Comment)
admin.site.register(Tag)
