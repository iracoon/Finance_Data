import pandas as pd 

from django.core.management.base import BaseCommand
from analysis.models import Compensation

class Command(BaseCommand):

    def add_arguments(self, parser): #python manage.py create_data PFDcomp.txt analysis_compensation
        parser.add_argument(
            'file_name', type=str, help='The txt file that contains the table records.')
        parser.add_argument(
            'model_name', type=str, help='The name of the table')

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        model_name = kwargs['model_name']

        if(model_name == "analysis_compensation"): #delete all records in table
            Compensation.objects.all().delete()

        num_rows = 0
            
        with open(f'{file_name}') as file: #read through each line in txt file, create a record, save 
            for row in file:
                cols = row.split('|,')
                tmp_arr = []

                for col in cols:
                    cleaned_col = col.replace('|', '').strip()
                    tmp_arr.append(cleaned_col)

                if(model_name == "analysis_compensation"):
                    comp_record = Compensation(
                        ID = tmp_arr[0],
                        Chamber = tmp_arr[1],
                        CID = tmp_arr[2],
                        CalendarYear = tmp_arr[3],
                        ReportType = tmp_arr[4],
                        CompSource = tmp_arr[5],
                        Orgname = tmp_arr[6],
                        Ultorg = tmp_arr[7],
                        Realcode = tmp_arr[8],
                        Source = tmp_arr[9],
                        CompSourceLocation = tmp_arr[10],
                        CompDuties = tmp_arr[11],
                        dupe = tmp_arr[12])
                    print(comp_record)
                    comp_record.save();
                    num_rows += 1;

        self.stdout.write(self.style.SUCCESS(str(num_rows) + ' records uploaded successfully!'))