

# Register your models here.
from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')  # removed 'submitted_at'
    ordering = ('name',)               # or any other existing field