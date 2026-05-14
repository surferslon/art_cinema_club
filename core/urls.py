from django.urls import path
from .views import MainView, CheckinCreateView

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("checkin/", CheckinCreateView.as_view(), name="checkin-create"),
]
