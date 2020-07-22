from django.contrib import admin

# Register your models here.
from .models import Word,Room

admin.site.register(Word)
admin.site.register(Room)