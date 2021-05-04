#### install all libraries
```
pip install -r requirements.txt
```

#### check migrations
```
python manage.py makemigrations
```
```
python manage.py migrate
```
#### create a web admin
```
python manage.py createsuperuser
```

#### (optional) create an new app
```
python manage.py startapp <app-name-here>
```
#### run the webserver
```
python manage.py runserver
```

#### local web server for testing mail 
```
python -m smtpd -n -c DebuggingServer localhost:1025
```