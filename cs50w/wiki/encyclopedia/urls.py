from django.urls import path
from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.get_page, name="entry"),
    path("search/", views.search, name="search_results"),
    path("new_page/", views.new_page, name="new_page"),
    path("edit/<str:title>",views.edit_page, name="edit_page"),
    path("random",views.random_page, name="random")
]

