from django.contrib import admin
from .models import Snack


@admin.register(Snack)
class AdminSnack(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'purchaser', ]
