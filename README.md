# pyruhr_quran

### buat environment baru, misal buat environment bernama "quran" menggunakan conda:

conda create -n quran python=3.7

### aktivkan environment yang sudah dibuat

conda activate quran

### install library yang dibutuhkan

pip install -r requirements.txt

### setup database

python manage.py makemigrations

python manage.py migrate

python manage.py shell < database_quran.py

### download file ayat (PNG), dan letakkan di dalam direktori "static"

https://drive.google.com/file/d/1f_UMC8UJkaK5_Hw_IQafoSLyq3JlMjBK/view?usp=sharing

### nyalakan server

python manage.py runserver

### akses localhost menggunakan web browser
