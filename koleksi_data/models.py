from django.db import models
from django.contrib.auth.models import User
 

class rekaman(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	no_surat = models.IntegerField()
	no_ayat = models.IntegerField()
	ukuran = models.IntegerField()
	filepath = models.CharField(max_length=200)
	waktu = models.DateTimeField(auto_now_add=True)

class data_surat(models.Model):
	no_surat = models.IntegerField()
	nama_surat = models.CharField(max_length=50)
	total_ayat = models.IntegerField()

class terjemah(models.Model):
	no_surat = models.IntegerField()
	no_ayat = models.IntegerField()
	terjemah = models.CharField(max_length=2000)