from django.urls import path
from Notification.views import home_view, api

from django.shortcuts import redirect

urlpatterns = [
    path("home/", home_view.home_view, name="home"),
    path("", lambda request: redirect("home")),
    path("subscribe", api.subscribe, name="subscribe"),
    path("subscriptions", api.get_subscriptions, name="get_subscriptions"),
]

