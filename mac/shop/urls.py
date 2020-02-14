from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="Shophome"),
    path("about/", views.about, name="Aboutus"),
    path("contact/", views.contact, name="Contactus"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="productview"),
    path("checkout/", views.checkout, name="Checkout"),
    #path("handlerequest/", views.handlerequest, name="handlerequest"),

]
