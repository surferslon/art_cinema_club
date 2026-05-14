from django.contrib import admin
from .models import ShowTime, Checkin


@admin.register(ShowTime)
class ShowTimeAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "seats")
    list_filter = ("date",)
    search_fields = ("title", "info")
    ordering = ("-date",)


@admin.register(Checkin)
class CheckinAdmin(admin.ModelAdmin):
    list_display = ("full_name", "showtime", "created_at")
    list_filter = ("showtime", "created_at")
    search_fields = ("full_name",)
    autocomplete_fields = ("showtime",)
