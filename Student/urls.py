from django.urls import path
from . import views
urlpatterns = [
    path('',views.indexStudent,name="HomeStudent")
]
