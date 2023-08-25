from django.urls import path

from . import views


app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("update/", views.update, name="update"),
    path("update-details/<int:id>/", views.update_detail, name="update_detail"),
    # path("update-details/<int:id>/", views.update_details, name="update_details"),
    path("contact/", views.contact, name="contact"),
    path("business_sectors/", views.sector, name="sector"),
    path("sector-details/<int:id>/", views.sector_detail, name="sector_detail"),
]
