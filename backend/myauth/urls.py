from django.urls import path
from . import views

urlpatterns = [
    path('update-form', views.update_form, name='update-form'),
]
