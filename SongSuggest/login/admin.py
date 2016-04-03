from django.contrib import admin

# Register your models here.
from .models import Suggestion, Vote

admin.site.register(Suggestion)
admin.site.register(Vote)