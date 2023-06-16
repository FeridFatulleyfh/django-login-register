from django.urls import path,NoReverseMatch

from . import views

urlpatterns = [
  
    path("logout",views.logout),
    path("signup",views.signup,name='signup'),
    path("login",views.login ,name='login'),
    path("contact",views.contact),
    path("admin",views.admin),
    path("",views.index2),
    path("index",views.index ,name='index'),
    path("error",views.error),
    path("blog",views.blog,name='blog'),
    path("about",views.about),
    path("index1",views.index1),
    path("portfolio",views.portfolio),
    path("single-blog",views.singleblog),
    path("single-portfolio",views.singleportfolio),
]
