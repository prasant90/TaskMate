
from django.contrib import admin
from django.urls import path,include
from todolist import views as todolist_views
from users_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',todolist_views.index, name='index'),
    path('todolist/',include('todolist.urls')),
    path('account/',include('users_app.urls')),
    path('about',todolist_views.about,name='about'),
    path('contact',todolist_views.contact,name='contact'),
]
