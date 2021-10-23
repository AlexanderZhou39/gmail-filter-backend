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
    data = pd.read_csv(file_path).fillna(value=False)

    new_rows = 0
    duplicate_rows = 0
    errored_rows = 0

    fields = {
        'name': 'string',
        'city': 'string', 
        'state': 'string', 
        'slug': 'string', 
        'acceptance': 'float', 
        'grad_rate': 'float', 
        'desirability': 'int', 
        'influence': 'int', 
        'overall_rank': 'int', 
        'sat': 'int',
        'act': 'int', 
        'undergrad_student_body': 'int', 
        'tuition': 'int'
    }

    for index, row in data.iterrows():
        College_dict = {}
        for key, value in fields.items():
            if row.get(key if not key == 'name' else 'school_name'):
                if value == 'int':
                    College_dict[key] = int(row.get(key))
                elif value == 'float':
                    College_dict[key] = float(row.get(key))
                else:
                    College_dict[key] = row.get(key if not key == 'name' else 'school_name')
        try:
            _, is_created = College.objects.get_or_create(
                domain=row.get('domain'),
                defaults=College_dict
            )
            new_rows += int(is_created)
            duplicate_rows += int(not is_created)
            # if not is_created:
            #     print(f'duplicate: {row.get("domain")}')

        except Exception as e:
            domain = row.get('domain')
            errored_rows += 1
            print(f'Error with index: {index} \n domain: {domain} \n :: {e} ::')
    
    print(f'\n\n==Results== \n new: {new_rows}\nduplicates: {duplicate_rows}\nerrors: {errored_rows}')

def delete_db():
    College.objects.all().delete()

if __name__ == '__main__':
    delete_db()
    populate_db('./data.csv')
    # print(College.objects.first().name)
