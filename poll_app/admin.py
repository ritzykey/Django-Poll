from django.contrib import admin
from .models import Poll

# Register your models here.

class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')
    list_display_links = ('id', 'question')
    list_per_page = 20




# Register your models here.

admin.site.register(Poll, PollAdmin)