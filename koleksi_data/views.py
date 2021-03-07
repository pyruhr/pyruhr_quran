# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import rekaman, data_surat, terjemah
from django.contrib.auth.models import User
from django.db.models import Sum
from time import time
import numpy as np
import json
import os




@login_required(login_url="/login/")
def history(request):
    db = rekaman.objects.filter(user=request.user.id).order_by('no_surat', 'no_ayat')
    list_nama_surat = [i.nama_surat for i in data_surat.objects.all()]
    max_ayat = [i.total_ayat for i in data_surat.objects.all()]
    ndb = []
    for e in db:
        tmp = {
            'pk': e.pk,
            'no_surat': e.no_surat, 
            'no_ayat': e.no_ayat, 
            'no_surat__no_ayat': f'{e.no_surat}__{e.no_ayat}',
            'ukuran': e.ukuran, 
            'waktu': e.waktu,
            'filepath': f'/{e.filepath}',
            'nama_surat': list_nama_surat[e.no_surat-1],
            'max_ayat': max_ayat[e.no_surat-1],
        }
        ndb.append(tmp)
    try:
        total_size = round(db.aggregate(Sum('ukuran'))['ukuran__sum']/1000, 2)
    except:
        total_size = 0
    data = {
        'db': ndb,
        'total_ayat': db.count(),
        'total_surat': db.order_by().values('no_surat').distinct().count(),
        'total_ukuran': total_size,
        'segment': 'history',
    }
    return render(request, 'history.html', data)


@login_required(login_url="/login/")
def delete_ayat(request, pk):
    if request.method == 'POST':
        dat = rekaman.objects.get(pk=pk)
        u = User.objects.get(username=dat.user)
        filePath = dat.filepath
        dat.delete()
        os.system(f'rm -f {filePath}')
    return redirect('history')


@login_required(login_url="/login/")
def record(request, no_surat__no_ayat):
    if no_surat__no_ayat == '0':
        no_surat = np.random.randint(low=1, high=114, size=1)[0]
        no_ayat =  np.random.randint(low=1, high=data_surat.objects.get(no_surat=no_surat).total_ayat, size=1)[0]
    else:
        no_surat = int(no_surat__no_ayat.split('__')[0])
        no_ayat = int(no_surat__no_ayat.split('__')[1])
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
        'segment': 'record',
    }     
    return render(request, 'record.html', data)


@login_required(login_url="/login/")
def upload(request):
    if request.method == 'POST':
        chars = 'abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        filePath = 'audio/' + str(time()).replace('.','')[:12] + "".join([chars[i] for j in range(8) for i in np.random.randint(0,len(chars),1)]) + '.wav'
        with open(filePath, 'wb') as file:
            file.write(request.body)
            data = request.headers['info'].split('_')
            b = User.objects.get(id=request.user.id)
            size = os.path.getsize(filePath)//1000
            try:
                # if data for particular "surat" & "ayat" already exist
                c = b.rekaman_set.get(no_surat=data[1], no_ayat=data[2])
                c.ukuran = size
                c.filepath = filePath
                c.save()
            except:
                # new entry
                b.rekaman_set.create(no_surat=data[1], no_ayat=data[2], ukuran=size, filepath=filePath)
        return redirect('history')





