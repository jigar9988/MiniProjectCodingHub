from django.contrib import admin
from django.urls import path, include
from CodingHub import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='index'),
    path("tutorial.html", views.tutorial, name='tutorial'),
    path("contact.html", views.contact, name='contact'),
    path("signup", views.handleSignUp, name='handleSignUp'),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('htuto.html', views.htuto, name="htuto"),
    path('csstuto.html', views.csstuto, name="csstuto"),
    path('jstuto.html', views.jstuto, name="jstuto"),
    path('java.html', views.java, name="java"),
    path('cpp.html', views.cpp, name="cpp"),
 ]
