from django.contrib import admin

from .models import CalendarEvent

class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ["title", "url", "css_class", "start", "end"]
    list_filler = ["title"]

admin.site.register(CalendarEvent, CalendarEventAdmin)
