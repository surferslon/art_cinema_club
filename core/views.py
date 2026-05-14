from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import Count, F, Value
from django.db.models.functions import Greatest

from showtimes.models import ShowTime, Checkin


class MainView(View):
    def get(self, request, *args, **kwargs):
        showtimes = (
            ShowTime.objects
            .filter(is_active=True)
            .annotate(seats_booked=Count("checkins"))
            .annotate(seats_left=Greatest(F("seats") - F("seats_booked"), Value(0)))
            .order_by("date")
        )
        context = {"showtimes": showtimes}
        return render(request, "core/main.html", context)


class CheckinCreateView(View):
    def post(self, request, *args, **kwargs):
        showtime_id = request.POST.get("showtime_id")
        full_name = request.POST.get("full_name", "").strip()
        showtime = (
            get_object_or_404(
                ShowTime.objects
                .annotate(seats_booked=Count("checkins"))
                .annotate(seats_left=Greatest(F("seats") - F("seats_booked"), Value(0))), pk=showtime_id,
            )
        )
        if full_name and showtime.seats_left > 0:
            Checkin.objects.create(full_name=full_name, showtime=showtime)

        return redirect("main")
