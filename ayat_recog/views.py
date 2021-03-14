# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render, redirect
from koleksi_data.models import data_surat, terjemah
from django.http import HttpResponse
from scipy.io.wavfile import read
from deepspeech import Model
import pandas as pd
import librosa
import json
import io


try:
    list_nama_surat = [f'{i.id}. {i.nama_surat_indo} ({i.nama_surat_arab})' for i in data_surat.objects.all()]
    max_ayat = [i.jumlah_ayat for i in data_surat.objects.all()]
    arti = {f'{i.no_surat}_{i.no_ayat}':i.terjemah for i in terjemah.objects.all()}
except:
    pass

# DeepSpeech Model
DSQ = Model('deepspeech/output_graph_imams_tusers_v2.pb')
DSQ.enableExternalScorer('deepspeech/quran.scorer')

# Text Quran Utsmani
df = pd.read_csv('data/quran_utsmani_no_basmalah.csv')
quran_dict = {f'{i[0]}_{i[1]}': i[2].split(' ') for i in df.values}

# search Ayat from quran_dict
def find_ayat(lookup):
    max_score = 0
    all_score = {}
    for key, value in quran_dict.items():
        score = 0
        for i in lookup:
            score += i in value
        match = score/len(value)
        all_score.update({key: (score, match)})
        if score > max_score:
            max_score = score
    if max_score > 0:
        result = { k:v for k, v in all_score.items() if v[0] == max_score }
    else:
        result = {}
    return result



def cari(request):
    data = {
        'segment': 'cari',
    }
    if request.method == 'POST':
        # audio recognition
        sr, signal = read(request.FILES['file'].file)
        prediction = DSQ.stt(signal)
        result = find_ayat(prediction.split(' '))
        # sorting based on similarity (high --> low)
        result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        data = {
            'result': json.dumps(result),
            'prediction': prediction,
            'list_nama_surat': json.dumps(list_nama_surat),
            'arti': json.dumps(arti),
            'segment': 'cari',
        }        
        return HttpResponse(json.dumps(data), content_type='application/json')
    return render(request, 'cari.html', data)



def hafalan(request):
    # arti = {f'{i.no_surat}_{i.no_ayat}':i.terjemah for i in terjemah.objects.all()}
    data = {
        'max_ayat': max_ayat,
        'list_nama_surat': json.dumps(list_nama_surat),
        # 'arti': json.dumps(arti),
        'quran_dict': json.dumps(quran_dict),
        'segment': 'hafalan',
    } 
    if request.method == 'POST':
        # audio recognition
        sr, signal = read(request.FILES['file'].file)
        prediction = DSQ.stt(signal).split(' ')
        data = {
            'prediction': prediction,
            'segment': 'hafalan',
        }
        return HttpResponse(json.dumps(data), content_type='application/json')     
    return render(request, 'hafalan.html', data)



def bacaan(request):
    # arti = {f'{i.no_surat}_{i.no_ayat}':i.terjemah for i in terjemah.objects.all()}
    data = {
        'max_ayat': max_ayat,
        'list_nama_surat': json.dumps(list_nama_surat),
        # 'arti': json.dumps(arti),
        'quran_dict': json.dumps(quran_dict),
        'segment': 'bacaan',
    } 
    if request.method == 'POST':
        # audio recognition
        sr, signal = read(request.FILES['file'].file)
        prediction = DSQ.stt(signal).split(' ')
        data = {
            'prediction': prediction,
            'segment': 'bacaan',
        }
        return HttpResponse(json.dumps(data), content_type='application/json')     
    return render(request, 'bacaan.html', data)

    