import csv
from django.core.management.base import BaseCommand
from dataentry.models import Student
from django.apps import apps
import datetime
from dataentry.utils import generate_csv_file

# propsed command = python manage.py exportdata model_name
class Command(BaseCommand):
    help = 'Export data from the database to a CSV file'


    def handle(self, *args, **kwargs):
        # fetch the data from the database
        #data = model.objects.all()
        students = Student.objects.all()


        # generate csv file path
            # generate the timestamp of current date and time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            # define the csv file name/path
        file_path = f'exported_student_data_{timestamp}.csv'

        # open the csv file and write the data
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)

            # write the CSV header
            # we want to print the field names of the model that we are trying to export
            #writer.writerow([field.name for field in model._meta.fields])
            writer.writerow(["Row No", "Name", "Age"])

            # write data rows
            for student in students:
                #writer.writerow([getattr(student, field.name) for field in model._meta.fields])
                writer.writerow([student.roll_no, student.name, student.age])

        
        self.stdout.write(self.style.SUCCESS('Data exported successfully!'))

# python manage.py exportdata-v1


