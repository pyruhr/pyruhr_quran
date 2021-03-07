# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('tahfidz/', views.tahfidz, name='tahfidz'),
    path('tajwid/', views.tajwid, name='tajwid'),
]