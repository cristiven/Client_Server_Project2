from django.contrib import admin

# Register your models here.
from .models import Room


admin.site.register(
    Room,
    list_display=["id", "label","active"],
    list_display_links=["id", "label","active"],
)