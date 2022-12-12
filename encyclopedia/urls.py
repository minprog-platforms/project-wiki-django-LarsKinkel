from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.entry, name="entry"),
    path("searched/", views.searchentry, name="searchentry"),
    path("createnew/", views.createnew, name="createnew"),
    path("createdpage/", views.createdpage, name="createdpage")
]
