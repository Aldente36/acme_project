# Blogicum
python -m venv venv
source venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

python manage.py loaddata db.json 
python manage.py createsuperuser
python manage.py startapp core