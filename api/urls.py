from django.urls import path
from .views import index, process_view

urlpatterns = [
    path('index/', index, name="index"),
    path('process/', process_view, name="process")
]
