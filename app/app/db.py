import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

POSTGRESQL = {
    'default' : {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME' : 'db',
        'USER' : 'postgres',
        'PASSWORD' : 'RodroE1345?',
        'HOST' : 'localhost',
        'PORT' : '5432'
    }
}