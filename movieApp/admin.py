from django.contrib import admin

# Register your models here.
from django.contrib import admin
from movieApp.models import Movie

class MovieAdmin(admin.ModelAdmin):
    search_fields = ["name"]

admin.site.register(Movie, MovieAdmin)