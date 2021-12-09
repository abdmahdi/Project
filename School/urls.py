from django.urls import path
from . import views
urlpatterns = [
    path('',views.indexSchool,name="HomeSchool")
]
