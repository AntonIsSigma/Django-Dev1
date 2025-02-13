from django.urls import path
from hello import views
from hello.models import LogMessage
from django.contrib import admin
from django.urls import path, include

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
    path("", home_list_view, name="home"),
    path("appointments/", views.appointments, name="appointments"),
    path("login/", views.login, name="login"),
    path("success_login/", views.success_login, name="success_login")
]