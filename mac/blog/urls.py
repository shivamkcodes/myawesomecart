from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="bloghome"),
    path("blogpage/<int:id>",views.blogpage,name="blogpage"),
    path("blogpage/<int:id>",views.blogpage,name="blogpage"),
    # path("writeblog",views.writeblog,name="writeblog"),
]