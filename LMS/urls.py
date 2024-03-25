
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

def manifest(request):
    manifest = {}
    with open("pwa/manifest.json", "r") as f:
        manifest = f.read()
    return HttpResponse(manifest, content_type="application/json")

def serviceworker(request):
    with open("pwa/serviceworker.js", "r") as f:
        serviceworker = f.read()
    return HttpResponse(serviceworker, content_type="application/x-javascript")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Notification.urls")),
    path(r'home/manifest.json', manifest),
    path(r'home/serviceworker.js', serviceworker),
]

