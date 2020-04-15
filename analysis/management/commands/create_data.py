import pandas as pd 

from django.core.management.base import BaseCommand
from analysis.models import Compensation
from analysis.models import Agreement
from analysis.models import Asset
from analysis.models import Gift
from analysis.models import Income
from analysis.models import Liability
from analysis.models import Position
from analysis.models import Transaction
from analysis.models import Travel
from analysis.models import Honoraria

# python manage.py makemigrations (1)
# python manage.py migrate (2)

#(3)
#python manage.py create_data data/PFDcomp.txt analysis_compensation
#python manage.py create_data data/PFDagree.txt analysis_agreement
#python manage.py create_data data/PFDasset.txt analysis_asset *** (millions of records-->takes long time)
#python manage.py create_data data/PFDgift.txt analysis_gift
#python manage.py create_data data/PFDincome.txt analysis_income
#python manage.py create_data data/PFDliability.txt analysis_liability
#python manage.py create_data data/PFDposition.txt analysis_position
#python manage.py create_data data/PFDtrans.txt analysis_transactions
#python manage.py create_data data/PFDtravel.txt analysis_travel
#python manage.py create_data data/PFDhonoraria.txt analysis_honoraria



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

                if(model_name == "analysis_asset"):
                    prev_ind = 0
                    all_rows = []
                    for row in file:
                        if row[0] != "|":
                            all_rows[prev_ind - 1] = all_rows[prev_ind - 1][:-1] + row
                        else:
                            all_rows.append(row)
                            prev_ind += 1

                    for row in all_rows:
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
                        comp_record = Asset(
                                ID = tmp_arr[0],
                                Chamber = tmp_arr[1],
                                CID = tmp_arr[2],
                                CalendarYear = tmp_arr[3],
                                ReportType = tmp_arr[4],
                                SenAB = tmp_arr[5],
                                AssetSpouseJointDep = tmp_arr[6],
                                AssetSource = tmp_arr[7],
                                Orgname = tmp_arr[8],
                                Ultorg = tmp_arr[9],
                                Realcode = tmp_arr[10],
                                Source = tmp_arr[11],
                                AssetDescrip = tmp_arr[12],
                                Orgname2 = tmp_arr[13],
                                Ultorg2 = tmp_arr[14],
                                Realcode2 = tmp_arr[15],
                                Source2 = tmp_arr[16],
                                AssetSourceLocation = tmp_arr[17],
                                AssetValue = tmp_arr[18],
                                AssetExactValue = tmp_arr[19],
                                AssetDividends = tmp_arr[20],
                                AssetRent = tmp_arr[21],
                                AssetInterest= tmp_arr[22],
                                AssetCapitalGains = tmp_arr[23],
                                AssetExemptedFund = tmp_arr[24],
                                AssetExemptedTrust = tmp_arr[24],
                                AssetQualifiedBlindTrust = tmp_arr[25],
                                AssetTypeCRP = tmp_arr[26],
                                OtherTypeIncome = tmp_arr[27],
                                AssetIncomeAmtRange = tmp_arr[28],
                                AssetIncomeAmountText = tmp_arr[29],
                                AssetIncomeAmt = tmp_arr[30],
                                AssetPurchased= tmp_arr[31],
                                AssetSold= tmp_arr[32],
                                AssetExchanged = tmp_arr[33],
                                AssetDate = tmp_arr[34],
                                AssetDateText = tmp_arr[35],
                                AssetNotes = tmp_arr[36],
                                Dupe = tmp_arr[37])
                        comp_record.save();
                        num_rows += 1;


                if(model_name == "analysis_gift"):
                    prev_ind = 0
                    all_rows = []
                    for row in file:
                        if row[0] != "|":
                            all_rows[prev_ind - 1] = all_rows[prev_ind - 1][:-1] + row
                        else:
                            all_rows.append(row)
                            prev_ind += 1

                    for row in all_rows:
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
                        comp_record = Gift(
                                ID = tmp_arr[0],
                                Chamber = tmp_arr[1],
                                CID = tmp_arr[2],
                                CalendarYear = tmp_arr[3],
                                ReportType = tmp_arr[4],
                                GiftSpouseJointDep = tmp_arr[5],
                                GiftSource = tmp_arr[6],
                                Orgname = tmp_arr[7],
                                Ultorg = tmp_arr[8],
                                Realcode = tmp_arr[9],
                                Source = tmp_arr[10],
                                GiftLocation = tmp_arr[11],
                                GiftDate = tmp_arr[12],
                                GiftDateText = tmp_arr[13],
                                GiftDescrip = tmp_arr[14],
                                GiftInfo = tmp_arr[15],
                                GiftValue = tmp_arr[16],
                                GiftValueText = tmp_arr[17],
                                Dupe = tmp_arr[18])
                        comp_record.save();
                        num_rows += 1;


                if(model_name == "analysis_income"):
                    prev_ind = 0
                    all_rows = []
                    for row in file:
                        if row[0] != "|":
                            all_rows[prev_ind - 1] = all_rows[prev_ind - 1][:-1] + row
                        else:
                            all_rows.append(row)
                            prev_ind += 1

                    for row in all_rows:
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
                        comp_record = Income(
                                ID = tmp_arr[0],
                                Chamber = tmp_arr[1],
                                CID = tmp_arr[2],
                                CalendarYear = tmp_arr[3],
                                ReportType = tmp_arr[4],
                                IncomeSource = tmp_arr[5],
                                Orgname = tmp_arr[6],
                                Ultorg = tmp_arr[7],
                                Realcode = tmp_arr[8],
                                Source = tmp_arr[9],
                                IncomeLocation = tmp_arr[10],
                                IncomeSpouseDep = tmp_arr[11],
                                IncomeType = tmp_arr[12],
                                IncomeAmt = tmp_arr[13],
                                IncomeAmtText = tmp_arr[14],
                                Dupe = tmp_arr[15])
                        comp_record.save();
                        num_rows += 1;


                if(model_name == "analysis_liability"):
                    prev_ind = 0
                    all_rows = []
                    for row in file:
                        if row[0] != "|":
                            all_rows[prev_ind - 1] = all_rows[prev_ind - 1][:-1] + row
                        else:
                            all_rows.append(row)
                            prev_ind += 1

                    for row in all_rows:
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
                        comp_record = Liability(
                                ID = tmp_arr[0],
                                Chamber = tmp_arr[1],
                                CID = tmp_arr[2],
                                CalendarYear = tmp_arr[3],
                                ReportType = tmp_arr[4],
                                LiabilitySpouseJointDep = tmp_arr[5],
                                Creditor = tmp_arr[6],
                                Orgname = tmp_arr[7],
                                Ultorg = tmp_arr[8],
                                Realcode = tmp_arr[9],
                                Source = tmp_arr[10],
                                TypeofLiability = tmp_arr[11],
                                LiabilityLoc = tmp_arr[12],
                                LiabilityDate = tmp_arr[13],
                                LiabilityDateText = tmp_arr[14],
                                LiabilityTerm = tmp_arr[15],
                                LiabilityInterestRate = tmp_arr[16],
                                LiabilityAmt = tmp_arr[17],
                                Dupe = tmp_arr[18])
                        comp_record.save();
                        num_rows += 1;


                if(model_name == "analysis_position"):
                    prev_ind = 0
                    all_rows = []
                    for row in file:
                        if row[0] != "|":
                            all_rows[prev_ind - 1] = all_rows[prev_ind - 1][:-1] + row
                        else:
                            all_rows.append(row)
                            prev_ind += 1

                    for row in all_rows:
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
                        comp_record = Position(
                                ID = tmp_arr[0],
                                Chamber = tmp_arr[1],
                                CID = tmp_arr[2],
                                CalendarYear = tmp_arr[3],
                                ReportType = tmp_arr[4],
                                PreviousPositions = tmp_arr[5],
                                PositionHeld = tmp_arr[6],
                                PositionOrg = tmp_arr[7],
                                Orgname = tmp_arr[8],
                                Ultorg = tmp_arr[9],
                                Realcode = tmp_arr[10],
                                Source = tmp_arr[11],
                                PositionOrgLoc = tmp_arr[12],
                                PositionOrgType = tmp_arr[13],
                                PositionFromDate = tmp_arr[14],
                                PositionFromDateText = tmp_arr[15],
                                PositionToDate = tmp_arr[16],
                                PositionToDateText = tmp_arr[17],
                                Dupe = tmp_arr[18])
                        comp_record.save();
                        num_rows += 1;

                if(model_name == "analysis_transactions"):
                    prev_ind = 0
                    all_rows = []
                    for row in file:
                        if row[0] != "|":
                            all_rows[prev_ind - 1] = all_rows[prev_ind - 1][:-1] + row
                        else:
                            all_rows.append(row)
                            prev_ind += 1

                    for row in all_rows:
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
                        try:
                            comp_record = Transaction(
                                    ID = tmp_arr[0],
                                    Chamber = tmp_arr[1],
                                    CID = tmp_arr[2],
                                    CalendarYear = tmp_arr[3],
                                    ReportType = tmp_arr[4],
                                    Asset4SJD = tmp_arr[5],
                                    Asset4Transacted = tmp_arr[6],
                                    Orgname = tmp_arr[7],
                                    Ultorg = tmp_arr[8],
                                    Realcode = tmp_arr[9],
                                    Source = tmp_arr[10],
                                    Asset4Descrip = tmp_arr[11],
                                    Orgname2 = tmp_arr[12],
                                    Ultorg2 = tmp_arr[13],
                                    Realcode2 = tmp_arr[14],
                                    Source2 = tmp_arr[15],
                                    Asset4Purchased = tmp_arr[16],
                                    Asset4Sold = tmp_arr[17],
                                    Asset4Exchanged = tmp_arr[18],
                                    Asset4Date = tmp_arr[19],
                                    Asset4DateText = tmp_arr[20],
                                    Asset4TransAmt = tmp_arr[21],
                                    Asset4ExactAmt = tmp_arr[22],
                                    CofD = tmp_arr[23],
                                    TransNotes = tmp_arr[24],
                                    Dupe = tmp_arr[25])
                            comp_record.save();
                            num_rows += 1;
                        except IndexError:
                            print("LIST INDEX ERROR OCCURED " + tmp_arr[0])
                        except:
                            print("SOME ERROR OCCURED HERE " + tmp_arr[0])


                if(model_name == "analysis_travel"):
                    prev_ind = 0
                    all_rows = []
                    for row in file:
                        if row[0] != "|":
                            all_rows[prev_ind - 1] = all_rows[prev_ind - 1][:-1] + row
                        else:
                            all_rows.append(row)
                            prev_ind += 1

                    for row in all_rows:
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
                        comp_record = Travel(
                                ID = tmp_arr[0],
                                Chamber = tmp_arr[1],
                                CID = tmp_arr[2],
                                CalendarYear = tmp_arr[3],
                                ReportType = tmp_arr[4],
                                TravelSource = tmp_arr[5],
                                Orgname = tmp_arr[6],
                                Ultorg = tmp_arr[7],
                                Realcode = tmp_arr[8],
                                Source = tmp_arr[9],
                                SourceCity = tmp_arr[10],
                                SourceState = tmp_arr[11],
                                BeginDate = tmp_arr[12],
                                BeginDateText = tmp_arr[13],
                                EndDate = tmp_arr[14],
                                EndDateText = tmp_arr[15],
                                DepartCity = tmp_arr[16],
                                DepartState = tmp_arr[17],
                                DestCity = tmp_arr[18],
                                DestState = tmp_arr[19],
                                PofRCity = tmp_arr[20],
                                PofRState = tmp_arr[21],
                                Descrip = tmp_arr[22],
                                Lodging = tmp_arr[23],
                                Food = tmp_arr[24],
                                FamilyIncl = tmp_arr[25],
                                TimeAtOwnExpense = tmp_arr[26],
                                Dupe = tmp_arr[27])
                        comp_record.save();
                        num_rows += 1;

                if(model_name == "analysis_honoraria"):
                    prev_ind = 0
                    all_rows = []
                    for row in file:
                        if row[0] != "|":
                            all_rows[prev_ind - 1] = all_rows[prev_ind - 1][:-1] + row
                        else:
                            all_rows.append(row)
                            prev_ind += 1

                    for row in all_rows:
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
                        comp_record = Honoraria(
                                ID = tmp_arr[0],
                                Chamber = tmp_arr[1],
                                CID = tmp_arr[2],
                                CalendarYear = tmp_arr[3],
                                ReportType = tmp_arr[4],
                                HonorariaSource = tmp_arr[5],
                                Orgname = tmp_arr[6],
                                Ultorg = tmp_arr[7],
                                Realcode = tmp_arr[8],
                                Source = tmp_arr[9],
                                HonorariaSourceLoc = tmp_arr[10],
                                HonorariaActivity = tmp_arr[11],
                                HonorariaDate = tmp_arr[12],
                                HonorariaDateText = tmp_arr[13],
                                HonorariaAmt = tmp_arr[14],
                                HonorariaAmtText = tmp_arr[15],
                                Dupe = tmp_arr[16])
                        comp_record.save();
                        num_rows += 1;

        self.stdout.write(self.style.SUCCESS(str(num_rows) + ' records uploaded successfully!'))