from django.contrib import admin

# Register your models here.

## to use models within the admin panel
from .models import Note

admin.site.register(Note)