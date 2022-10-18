from django.contrib import admin
from app_media.models import Profile, Entry, EntryImage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'number', 'city')

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(EntryImage)
class EntryImageAdmin(admin.ModelAdmin):
    pass
