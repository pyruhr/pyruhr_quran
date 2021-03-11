from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from koleksi_data.models import rekaman
from autentikasi.models import Profile
import pandas as pd


TARGET_AYAT = 10_000


def home(request): 
    return redirect('dashboard')


def dashboard(request):

	# build dataframe from database
	df_ayat = pd.DataFrame(list(rekaman.objects.all().values()))
	df_user = pd.DataFrame(list(User.objects.all().values('id', 'username')))
	df_user =  df_user[df_user['username']!='admin']
	df_profile = pd.DataFrame(list(Profile.objects.all().values()))
	# merge df_user & df_profile
	df_user = df_user.merge(df_profile.drop(['id'], axis=1), how='left', left_on='id', right_on='user_id')
	df_user.drop(['user_id'], axis=1, inplace=True)
	# merge df_user & df_ayat
	df = df_user.merge(df_ayat.drop(['id'], axis=1), how='left', left_on='id', right_on='user_id')
	df.drop(['user_id'], axis=1, inplace=True)
	# reset index
	df = df.set_index('id')
	df_user = df_user.set_index('id')


    # data (summary)
	total_user = len(df_user)
	total_ayat = len(df_ayat)
	total_surat = len(df_ayat.groupby('no_surat'))
	persen_target = round(total_ayat / TARGET_AYAT * 100, 2)
	try:
	    total_data = round(df_ayat['ukuran'].sum() / 1e6, 2) # GB
	except:
	    total_data = 0
	prediksi_data_target = round(df_ayat['ukuran'].mean() * TARGET_AYAT / 1e6, 2) # GB

	# data (top5 user)
	top5 = df_ayat.groupby('user_id').size().sort_values(ascending=False)
	data_top5 = []
	for i in range(5):
		user_id = top5.index[i]
		tmp = {
			'username': df_user.loc[user_id,'username'],
			'jumlah_ayat': top5[user_id],
			'jumlah_surat': df_ayat[df_ayat['user_id']==user_id]['no_surat'].nunique(),
			'lembaga': df_user.loc[user_id,'lembaga'],
			}
		data_top5.append(tmp)

	# data lembaga
	data_lembaga = []
	group_user_lembaga = df_user.groupby('lembaga').size().sort_values(ascending=False)
	jumlah_kontributor_dict = dict(group_user_lembaga)
	jumlah_ayat_dict = dict(df.groupby('lembaga').size())
	jumlah_surat_dict = dict(df.groupby('lembaga')['no_surat'].nunique())
	for l in group_user_lembaga.index:
		tmp = {
			'lembaga': l,
			'jumlah_kontributor': jumlah_kontributor_dict[l],
			'jumlah_ayat': jumlah_ayat_dict[l],
			'jumlah_surat': jumlah_surat_dict[l],
			}
		data_lembaga.append(tmp)

	# payload
	data = {
		# data (summary)
		'total_user': total_user,
		'total_ayat': total_ayat,
		'total_surat': total_surat,
		'total_data': total_data,
		'persen_target': persen_target,
		'target_ayat': TARGET_AYAT,
		'prediksi_data_target': prediksi_data_target,
		# data (top5 user)
		'top5_user': data_top5,
		# data lembaga
		'lembaga': data_lembaga,
		# segment
	    'segment': 'dashboard',
	}  

	return render(request, 'dashboard.html', data)



