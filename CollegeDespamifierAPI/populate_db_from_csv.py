import os
import sys 
import pandas as pd
import numpy as np

base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_dir)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CollegeDespamifierAPI.settings')
application = get_wsgi_application()

from CollegeApp.models import College

def populate_db(file_path):
    data = pd.read_csv(file_path)

    for row in dataframe:
        try:
            College.objects.get_or_create(
                domain=row['domain']
                defaults={
                    'state': row['state']
                }
            )
    print(data.head())



if __name__ == '__main__':
    populate_db('./data.csv')
