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

### nyalakan server

python manage.py runserver

### akses localhost menggunakan web browser
