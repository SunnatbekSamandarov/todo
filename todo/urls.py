from django.contrib import admin
from django.urls import path,include
from .views import index,create,update,delete
urlpatterns = [
    path('home/',index ,name = 'home'),
    path('create/',create ,name = 'create'),
    path("update/<int:pk>/", update, name="update"),
    path("delete/<int:pk>/", delete, name="delete"),
]
