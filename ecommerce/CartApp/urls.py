from django.urls import path
from CartApp import views
urlpatterns=[
    path("",views.IndexView.as_view(),name="home"),
    path("carts",views.CartsView.as_view(),name="carts"),
    path("carts/add/<int:id>",views.AddToCart.as_view(),name="addtocart"),
]