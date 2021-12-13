# versi
Ubuntu 20.04

Python 3.8.10

gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0

# apt awal
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

sudo apt-get install sqlite3 libsqlite3-dev

sudo apt-get install mysql-server

sudo apt-get install python3-dev libmysqlclient-dev

# langkah-langkah
## install all modul python
pip install -r requirement.txt
## create user untuk /admin
python3 manage.py createsuperuser
## migration database
python3 manage.py makemigrations

python3 manage.py migrate
## runserver
python3 manage.py runserver
admin:Mudahcoding8181?
