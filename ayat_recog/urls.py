# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('cari/', views.cari, name='cari'),
    path('hafalan/', views.hafalan, name='hafalan'),
    path('bacaan/', views.bacaan, name='bacaan'),
]