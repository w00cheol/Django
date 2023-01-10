from mimetypes import guess_all_extensions
from django.contrib import admin

# Register your models here.
from .models import GuessNumbers

admin.site.register(GuessNumbers)