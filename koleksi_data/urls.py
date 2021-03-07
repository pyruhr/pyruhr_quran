# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('record/<str:no_surat__no_ayat>/', views.record, name='record'),
    path('upload/', views.upload, name='upload'),
    path('history/', views.history, name='history'),
    path('history/delete/<int:pk>/', views.delete_ayat, name='delete_ayat'),
]