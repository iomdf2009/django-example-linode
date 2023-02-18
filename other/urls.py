from django.urls import path
from other import views

urlpatterns = [
    path('', views.simply_view),
]