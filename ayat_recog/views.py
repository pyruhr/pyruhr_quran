# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render
from koleksi_data.models import data_surat, terjemah
import json



def search(request):
    no_surat = 1
    no_ayat = 1
    list_nama_surat = [i.nama_surat for i in data_surat.objects.all()]
    max_ayat = [i.total_ayat for i in data_surat.objects.all()]
    arti = {f'{i.no_surat}_{i.no_ayat}':i.terjemah for i in terjemah.objects.all()}
    data = {
        'no_surat': no_surat,
        'nama_surat': list_nama_surat[no_surat-1],
        'no_ayat': no_ayat,
        'list_nama_surat': json.dumps(list_nama_surat),
        'arti': json.dumps(arti),
        'terjemah': arti[f'{no_surat}_{no_ayat}'] + f'  (QS {no_surat} : {no_ayat})',
        'file_img' : f'/static/all_ayat/{no_surat}_{no_ayat}.png',
        'segment': 'search',
    }     
    return render(request, 'search.html', data)



def tahfidz(request):
    no_surat = 1
    no_ayat = 1
    list_nama_surat = [i.nama_surat for i in data_surat.objects.all()]
    max_ayat = [i.total_ayat for i in data_surat.objects.all()]
    arti = {f'{i.no_surat}_{i.no_ayat}':i.terjemah for i in terjemah.objects.all()}
    data = {
        'no_surat': no_surat,
        'nama_surat': list_nama_surat[no_surat-1],
        'no_ayat': no_ayat,
        'list_nama_surat': json.dumps(list_nama_surat),
        'arti': json.dumps(arti),
        'terjemah': arti[f'{no_surat}_{no_ayat}'] + f'  (QS {no_surat} : {no_ayat})',
        'file_img' : f'/static/all_ayat/{no_surat}_{no_ayat}.png',
        'segment': 'tahfidz',
    }     
    return render(request, 'tahfidz.html', data)



def tajwid(request):
    no_surat = 1
    no_ayat = 1
    list_nama_surat = [i.nama_surat for i in data_surat.objects.all()]
    max_ayat = [i.total_ayat for i in data_surat.objects.all()]
    arti = {f'{i.no_surat}_{i.no_ayat}':i.terjemah for i in terjemah.objects.all()}
    data = {
        'no_surat': no_surat,
        'nama_surat': list_nama_surat[no_surat-1],
        'no_ayat': no_ayat,
        'list_nama_surat': json.dumps(list_nama_surat),
        'max_ayat': max_ayat,
        'arti': json.dumps(arti),
        'terjemah': arti[f'{no_surat}_{no_ayat}'] + f'  (QS {no_surat} : {no_ayat})',
        'file_img' : f'/static/all_ayat/{no_surat}_{no_ayat}.png',
        'segment': 'tajwid',
    }     
    return render(request, 'tajwid.html', data)