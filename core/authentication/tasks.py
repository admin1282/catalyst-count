# authentication/tasks.py
import pandas as pd
from celery import shared_task
from .models import Company
from django.core.files.storage import FileSystemStorage
import csv
import os


import pandas as pd

@shared_task
def process_csv_file(file_path, user_id):
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return f"Error reading CSV file: {e}"

    # Check DataFrame columns
    print(f"Columns in DataFrame: {df.columns}")
    for index, row in df.iterrows():
        print(f"Saving row: {row}")  
        current_employee_estimate = row.get('current employee estimate', 0)  
        total_employee_estimate = row.get('total employee estimate', 0)  
        year_founded = row.get('year founded', None)

        index_val = row.get('index', 0)  
        name = row.get('name', "Null")  
        domain = row.get('domain', "Null")  
        industry = row.get('industry', "Unknown")  
        size_range = row.get('size range', "Unknown")  
        locality = row.get('locality', "Unknown")  
        country = row.get('country', "Unknown")  
        linkedin_url = row.get('linkedin url', None)  

        Company.objects.update_or_create(
            user_id=user_id,
            index=index_val,  
            name=name,  
            domain=domain, 
            year_founded=year_founded,  
            industry=industry,  
            size_range=size_range,  
            locality=locality,  
            country=country,  
            linkedin_url=linkedin_url,  
            current_employee_estimate=current_employee_estimate,  
            total_employee_estimate=total_employee_estimate,  
        )

    return f"Processed file {file_path} successfully"
