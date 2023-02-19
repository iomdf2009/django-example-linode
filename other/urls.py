from django.urls import path
from other.views import HomeView

app_name = "other"

urlpatterns = [
    path('', HomeView.as_view(), name="HomeView"),
]