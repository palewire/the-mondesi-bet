from django.contrib import admin
from django.urls import path
from scrape import views


urlpatterns = [
    path('season-totals.json', views.seasontotals_latest, name="index"),
    path('admin/', admin.site.urls),
]
