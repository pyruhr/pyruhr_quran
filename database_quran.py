from koleksi_data.models import data_surat, terjemah
import pandas as pd

# data surat
df = pd.read_csv('data/info_surat.csv')
for i in range(len(df)):
	data_surat.objects.create(no_surat=df.iloc[i,0], nama_surat_arab=df.iloc[i,1], nama_surat_indo=df.iloc[i,2], jumlah_ayat=df.iloc[i,3])

# terjemah
df = pd.read_csv('data/terjemah_edit.csv')
for i in range(len(df)):
	terjemah.objects.create(no_surat=df.loc[i,'surat'], no_ayat=df.loc[i,'ayat'], terjemah=df.loc[i,'terjemah'])
