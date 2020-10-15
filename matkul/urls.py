from os import name
from matkul.views import tambah
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tambah/', views.tambah, name="tambah"),
    path("<int:semester_id>", views.semester, name="semester")
]