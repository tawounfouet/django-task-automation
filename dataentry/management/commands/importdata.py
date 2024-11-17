from django.core.management.base import BaseCommand, CommandError
from dataentry.models import Student
from django.apps import apps
import csv
from django.db import DataError
from dataentry.utils import check_csv_errors

# Proposed command - python manage.py importdata file_path model_name

class Command(BaseCommand):
    help = "Import data from CSV file"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
        parser.add_argument('model_name', type=str, help='Name of the model')

    def handle(self, *args, **kwargs):
        # logic goes here
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()

        model = check_csv_errors(file_path, model_name)
        
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            # print(reader)
            for row in reader:
                # print(row)
                #Student.objects.create(**row)
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data imported from CSV successfully!'))

# python manage.py importdata

# resources/data/student_data.csv
# /workspaces/django-task-automation/resources/data/student_data.csv

# python manage.py importdata /workspaces/django-task-automation/resources/data/student_data.csv