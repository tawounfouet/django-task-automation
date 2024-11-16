

```sh
python3 -m venv _venv

source _venv/bin/activate

# python --version
# Python 3.12.1

pip install django

pip install python-decouple django-autocomplete-light
pip install django-crispy-forms
pip install crispy-bootstrap5
pip install django-ckeditor
pip install django-anymail
pip install beautifulsoup4
pip install pillow

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
#Username (leave blank to use 'codespace'): admin
# Email address: admin@example.com
#Password: admin
#Password (again): admin