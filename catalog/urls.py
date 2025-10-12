from django.urls import path

from catalog import views
from catalog.apps import AppNameConfig
from catalog.views import contacts, home, portfolio

app_name = AppNameConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("portfolio/", portfolio, name="portfolio"),
    path("product_detail/<int:pk>", views.product_detail, name="product_detail")
]
