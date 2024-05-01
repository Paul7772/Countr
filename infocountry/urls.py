from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:country_slug>/', views.show_descript)
]