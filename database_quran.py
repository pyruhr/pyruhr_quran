from koleksi_data.models import data_surat, terjemah
import pandas as pd

# data surat
df = pd.read_csv('nama_surat.csv', header=None)
for i in range(len(df)):
	data_surat.objects.create(no_surat=df.loc[i,0], nama_surat=df.loc[i,1], total_ayat=df.loc[i,2])

# terjemah
df = pd.read_csv('terjemah_edit.csv')
for i in range(len(df)):
	terjemah.objects.create(no_surat=df.loc[i,'surat'], no_ayat=df.loc[i,'ayat'], terjemah=df.loc[i,'terjemah'])
