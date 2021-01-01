from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("call_back/", views.call_back, name = "call_back")
]