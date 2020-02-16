import pandas as pd 

from django.core.management.base import BaseCommand
from analysis.models import Compensation

class Command(BaseCommand):



    def add_arguments(self, parser):
        parser.add_argument(
            'file_name', type=str, help='The txt file that contains the table records.')
        parser.add_argument(
            'model_name', type=str, help='The name of the table')

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        model_name = kwargs['model_name']

        with open(f'{file_name}') as file:
            for row in file:
                cols = row.split('|,')
                for col in cols:
                    cleaned_col = col[1:]
                    print('>'+ cleaned_col)
                print('\n\n')