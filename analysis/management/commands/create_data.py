import pandas as pd 

from django.core.management.base import BaseCommand
from analysis.models import Compensation
from analysis.models import Agreement

# python manage.py makemigrations (1)
# python manage.py migrate (2)

#(3)
#python manage.py create_data data/PFDcomp.txt analysis_compensation
#python manage.py create_data data/PFDagree.txt analysis_agreement

class Command(BaseCommand):

    def add_arguments(self, parser): 
        parser.add_argument(
            'file_name', type=str, help='The txt file that contains the table records.')
        parser.add_argument(
            'model_name', type=str, help='The name of the table')

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        model_name = kwargs['model_name']

        if(model_name == "analysis_compensation"): #delete all records in table
            Compensation.objects.all().delete()

        if(model_name == "analysis_agreement"): #delete all records in table
            Agreement.objects.all().delete()

        num_rows = 0
            
        with open(f'{file_name}') as file: #read through each line in txt file, create a record, save 
                if(model_name == "analysis_compensation"):
                    for row in file:
                        cols = row.split('|,')
                        tmp_arr = []
                        for col in cols:
                            cleaned_col = col.replace('|', '').strip()
                            tmp_arr.append(cleaned_col)
                        print(tmp_arr)
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
                        comp_record.save();
                        num_rows += 1;

                if(model_name == "analysis_agreement"):
                    prev_ind = 0
                    all_rows = []
                    for row in file:
                        if row[0] != "|":
                            all_rows[prev_ind - 1] = all_rows[prev_ind - 1][:-1] + row
                        else:
                            all_rows.append(row)
                            prev_ind += 1

                    for row in all_rows:
                        print(row)
                        tmp_arr = []
                        isStringWord = False
                        word = ""
                        for char in row:
                            if char == row[-1]:
                                tmp_arr.append(word)
                            if char == "," and isStringWord == False:
                                tmp_arr.append(word)
                                word = ""
                            elif char == "," and isStringWord == True:
                                word += char
                            elif char == "|" and isStringWord == False:
                                isStringWord = True
                            elif char == "|" and isStringWord == True:
                                isStringWord = False
                            else:
                                word += char
                        print(tmp_arr)
                        print(tmp_arr[21])
                        comp_record = Agreement(
                            ID = tmp_arr[0],
                            Chamber = tmp_arr[1],
                            CID = tmp_arr[2],
                            CalendarYear = tmp_arr[3],
                            ReportType = tmp_arr[4],
                            AgreementDate1 = tmp_arr[5],
                            AgreementDate1Text = tmp_arr[6],
                            AgreementDate2 = tmp_arr[7],
                            AgreementDate2Text = tmp_arr[8],
                            AgreementParty1 = tmp_arr[9],
                            Orgname = tmp_arr[10],
                            Ultorg = tmp_arr[11],
                            Realcode = tmp_arr[12],
                            Source = tmp_arr[13],
                            AgreementParty1Loc = tmp_arr[14],
                            AgreementParty2 = tmp_arr[15],
                            Orgname2 = tmp_arr[16],
                            Ultorg2 = tmp_arr[17],
                            Realcode2 = tmp_arr[18],
                            Source2 = tmp_arr[19],
                            AgreementTerms = tmp_arr[20],
                            dupe = tmp_arr[21])
                        comp_record.save();
                        num_rows += 1;

        self.stdout.write(self.style.SUCCESS(str(num_rows) + ' records uploaded successfully!'))