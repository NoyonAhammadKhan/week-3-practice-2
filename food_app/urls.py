from django.urls import path, include
from . import views
urlpatterns = [

    path("", views.show_menu, name="show_menu"),
]
