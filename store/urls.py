from django.urls import path
from store.views import homepage,product_details, category_filtering,product_search
urlpatterns = [
    # path("",homepage),
    path("",homepage, name="home"),
    path("product-details/<str:slug>/",product_details, name="product_details"),
    path("category-filtering/<int:id>/",category_filtering, name="category_filtering"),
    path("product-search/",product_search, name="product_search"),


]