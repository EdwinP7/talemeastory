from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Excerpt)
class ExcerptAdmin(admin.ModelAdmin):
    pass
