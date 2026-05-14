from django.db import models


class ShowTime(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=200)
    info = models.TextField(blank=True)
    seats = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.title} @ {self.date:%Y-%m-%d %H:%M}"


class Checkin(models.Model):
    full_name = models.CharField(max_length=200)
    showtime = models.ForeignKey(ShowTime, on_delete=models.CASCADE, related_name="checkins")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.full_name} – {self.showtime}"
