from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# drop tables if they already exist
# delete old migration files for table if they exist
# DELETE FROM finance_data.django_migrations WHERE app='analysis';
# python ./manage.py makemigrations analysis (1)
# python ./manage.py migrate analysis (2)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('analysis-research-detail', kwargs={'pk': self.pk})


class Compensation(models.Model):
	ID = models.CharField(max_length=15, primary_key=True)
	Chamber = models.CharField(max_length=1, default=None)
	CID = models.CharField(max_length=9, default=None)
	CalendarYear = models.CharField(max_length=2, default=None)
	ReportType = models.CharField(max_length=1, default=None)
	CompSource = models.CharField(max_length=100, default=None)
	Orgname = models.CharField(max_length=50, default=None) #changed from 40->60 to accomadate some long org names
	Ultorg = models.CharField(max_length=40, default=None)
	Realcode = models.CharField(max_length=5, default=None)
	Source = models.CharField(max_length=5, default=None)
	CompSourceLocation = models.CharField(max_length=50, default=None)
	CompDuties = models.CharField(max_length=100, default=None)
	dupe = models.CharField(max_length=1,default=None)

	
	def __str__(self):
		obj_str = 'ID: ' + self.ID + '  ' + \
		'Chamber: ' + self.Chamber + '  ' + \
		'CID: ' + self.CID + '  ' + \
		'CalendarYear: ' + self.CalendarYear + '  ' + \
		'ReportType: ' + self.ReportType + '  ' + \
		'CompSource: ' + self.CompSource + '  ' + \
		'Orgname: ' + self.Orgname + '  ' + \
		'Ultorg: ' + self.Ultorg + '  ' + \
		'Realcode: ' + self.Realcode + '  ' + \
		'Source: ' + self.Source + '  ' + \
		'CompSourceLocation: ' + self.CompSourceLocation + '  ' + \
		'CompDuties: ' + self.CompDuties + '  ' + \
		'dupe: ' + self.dupe + '\n\n  ' 
		return obj_str

# CREATE TABLE [dbo].[Compensation](
# [ID] [varchar](15) NOT NULL,
# [Chamber] [char](1) NULL,
# [CID] [char](9) NULL,
# [CalendarYear] [char](2) NULL,
# [ReportType] [char](1) NULL,
# [CompSource] [varchar](100) NULL,
# [Orgname] [varchar](40) NULL,
# [Ultorg] [varchar](40) NULL,
# [Realcode] [char](5) NULL,
# [Source] [char](5) NULL,
# [CompSourceLocation] [varchar](50) NULL,
# [CompDuties] [varchar](100) NULL,
# [dupe] [char](1) NULL
# ) ON [PRIMARY]

########################################################

class Agreement(models.Model):
	ID = models.CharField(max_length=15, primary_key=True)
	Chamber = models.CharField(max_length=1, default=None)
	CID = models.CharField(max_length=9, default=None)
	CalendarYear = models.CharField(max_length=2, default=None)
	ReportType = models.CharField(max_length=1, default=None)
	AgreementDate1 = models.CharField(max_length=100,default=None)
	AgreementDate1Text = models.CharField(max_length=100, default=None)
	AgreementDate2 = models.CharField(max_length=100, default=None)
	AgreementDate2Text = models.CharField(max_length=100, default=None)
	AgreementParty1 = models.CharField(max_length=100, default=None)
	Orgname = models.CharField(max_length=100, default=None)
	Ultorg = models.CharField(max_length=100, default=None)
	Realcode = models.CharField(max_length=100, default=None)
	Source = models.CharField(max_length=100, default=None)
	AgreementParty1Loc = models.CharField(max_length=100, default=None)
	AgreementParty2 = models.CharField(max_length=100, default=None)
	Orgname2 = models.CharField(max_length=100, default=None)
	Ultorg2 = models.CharField(max_length=100, default=None)
	Realcode2 = models.CharField(max_length=100, default=None)
	Source2 = models.CharField(max_length=100, default=None)
	AgreementTerms = models.TextField(default=None)
	dupe = models.CharField(max_length=1,default=None)

	def __str__(self):
		obj_str = 'ID: ' + self.ID 
		return obj_str

# CREATE TABLE [dbo].[Agreement](
# [ID] [varchar](15) NOT NULL,
# [Chamber] [char](1) NULL,
# [CID] [char](9) NULL,
# [CalendarYear] [char](2) NOT NULL,
# [ReportType] [char](1) NULL,
# [AgreementDate1] [smalldatetime] NULL,
# [AgreementDate1Text] [char](50) NULL,
# [AgreementDate2] [smalldatetime] NULL,
# [AgreementDate2Text] [char](50) NULL,
# [AgreementParty1] [varchar](100) NULL,
# [Orgname] [varchar](40) NULL,
# [Ultorg] [varchar](40) NULL,
# [Realcode] [char](5) NULL,
# [Source] [char](5) NULL,
# [AgreementParty1Loc] [varchar](50) NULL,
# [AgreementParty2] [varchar](100) NULL,
# [Orgname2] [varchar](40) NULL,
# [Ultorg2] [varchar](40) NULL,
# [Realcode2] [char](5) NULL,
# [Source2] [char](5) NULL,
# [AgreementTerms] [varchar](1500) NULL,
# [Dupe] [char](1) NULL
# ) ON [PRIMARY]

###############################################

class Asset(models.Model):
	ID = models.CharField(max_length=15, primary_key=True)
	Chamber = models.CharField(max_length=1, default=None)
	CID = models.CharField(max_length=9, default=None)
	CalendarYear = models.CharField(max_length=2, default=None)
	ReportType = models.CharField(max_length=1, default=None)
	SenAB = models.CharField(max_length=1, default=None)
	AssetSpouseJointDep = models.CharField(max_length=1, default=None)
	AssetSource = models.CharField(max_length=100, default=None)
	Orgname = models.CharField(max_length=100, default=None)
	Ultorg = models.CharField(max_length=100, default=None)
	Realcode = models.CharField(max_length=100, default=None)
	Source = models.CharField(max_length=100, default=None)
	AssetDescrip = models.CharField(max_length=100, default=None)
	Orgname2 = models.CharField(max_length=100, default=None)
	Ultorg2 = models.CharField(max_length=100, default=None)
	Realcode2 = models.CharField(max_length=100, default=None)
	Source2 = models.CharField(max_length=50, default=None)
	AssetSourceLocation = models.CharField(max_length=100, default=None)
	AssetValue = models.CharField(max_length=5, default=None)
	AssetExactValue = models.CharField(max_length=100, default=None)
	AssetDividends = models.CharField(max_length=1, default=None)
	AssetRent = models.CharField(max_length=1, default=None)
	AssetInterest= models.CharField(max_length=1, default=None)
	AssetCapitalGains = models.CharField(max_length=1, default=None)
	AssetExemptedFund = models.CharField(max_length=1, default=None)
	AssetExemptedTrust = models.CharField(max_length=1, default=None)
	AssetQualifiedBlindTrust = models.CharField(max_length=1, default=None)
	AssetTypeCRP = models.CharField(max_length=2, default=None)
	OtherTypeIncome = models.CharField(max_length=100, default=None)
	AssetIncomeAmtRange = models.CharField(max_length=100, default=None)
	AssetIncomeAmountText = models.CharField(max_length=100, default=None)
	AssetIncomeAmt = models.CharField(max_length=100, default=None)
	AssetPurchased= models.CharField(max_length=1, default=None)
	AssetSold= models.CharField(max_length=1, default=None)
	AssetExchanged = models.CharField(max_length=1, default=None)
	AssetDate = models.CharField(max_length=100, default=None)
	AssetDateText = models.CharField(max_length=100, default=None)
	AssetNotes = models.CharField(max_length=100, default=None)
	Dupe = models.CharField(max_length=1, default=None)
	

	def __str__(self):
		obj_str = 'ID: ' + self.ID 
		return obj_str

# CREATE TABLE [dbo].[PFD_Asset](
# [ID] [varchar](15) NOT NULL,
# [Chamber] [char](1) NULL,
# [CID] [char](9) NULL,
# [CalendarYear] [char](2) NOT NULL,
# [ReportType] [char](1) NULL,
# [SenAB] [char](1) NULL,
# [AssetSpouseJointDep] [char](1) NULL,
# [AssetSource] [varchar](100) NULL,
# [Orgname] [varchar](40) NULL,
# [Ultorg] [varchar](40) NULL,
# [Realcode] [char](5) NULL,
# [Source] [char](5) NULL,
# [AssetDescrip] [varchar](100) NULL,
# [Orgname2] [varchar](40) NULL,
# [Ultorg2] [varchar](40) NULL,
# [Realcode2] [char](5) NULL,
# [Source2] [char](5) NULL,
# [AssetSourceLocation] [varchar](50) NULL,
# [AssetValue] [char](2) NULL,
# [AssetExactValue] [decimal](18, 0) NULL,
# [AssetDividends] [char](1) NULL,
# [AssetRent] [char](1) NULL,
# [AssetInterest] [char](1) NULL,
# [AssetCapitalGains] [char](1) NULL,
# [AssetExemptedFund] [char](1) NULL,
# [AssetExemptedTrust] [char](1) NULL,
# [AssetQualifiedBlindTrust] [char](1) NULL,
# [AssetTypeCRP] [char](2) NULL,
# [OtherTypeIncome] [varchar](100) NULL,
# [AssetIncomeAmtRange] [varchar](4) NULL,
# [AssetIncomeAmountText] [varchar](10) NULL,
# [AssetIncomeAmt] [money] NULL,
# [AssetPurchased] [char](1) NULL,
# [AssetSold] [char](1) NULL,
# [AssetExchanged] [char](1) NULL,
# [AssetDate] [smalldatetime] NULL,
# [AssetDateText] [varchar](25) NULL,
# [AssetNotes] [varchar](100) NULL,
# [Dupe] [char](1) NULL

########################################################

class Gift(models.Model):
	ID = models.CharField(max_length=15, primary_key=True)
	Chamber = models.CharField(max_length=1, default=None)
	CID = models.CharField(max_length=9, default=None)
	CalendarYear = models.CharField(max_length=2, default=None)
	ReportType = models.CharField(max_length=1, default=None)
	GiftSpouseJointDep = models.CharField(max_length=1, default=None)
	GiftSource = models.CharField(max_length=250, default=None)
	Orgname = models.CharField(max_length=60, default=None)
	Ultorg = models.CharField(max_length=50, default=None)
	Realcode = models.CharField(max_length=20, default=None)
	Source = models.CharField(max_length=20, default=None)
	GiftLocation = models.CharField(max_length=70, default=None)
	GiftDate = models.CharField(max_length=20, default=None)
	GiftDateText = models.CharField(max_length=30, default=None)
	GiftDescrip = models.CharField(max_length=250, default=None)
	GiftInfo = models.CharField(max_length=150, default=None)
	GiftValue = models.CharField(max_length=20, default=None)
	GiftValueText = models.CharField(max_length=70, default=None)
	Dupe = models.CharField(max_length=1, default=None)


	def __str__(self):
		obj_str = 'ID: ' + self.ID 
		return obj_str

# CREATE TABLE [dbo].[Gift](
# [ID] [varchar](15) NOT NULL,
# [Chamber] [char](1) NULL,
# [CID] [char](9) NULL,
# [CalendarYear] [char](2) NULL,
# [ReportType] [char](1) NULL,
# [GiftSpouseJointDep] [char](1) NULL,
# [GiftSource] [varchar](200) NULL,
# [Orgname] [varchar](40) NULL,
# [Ultorg] [varchar](40) NULL,
# [Realcode] [char](5) NULL,
# [Source] [char](5) NULL,
# [GiftLocation] [varchar](50) NULL,
# [GiftDate] [smalldatetime] NULL,
# [GiftDateText] [varchar](20) NULL,
# [GiftDescrip] [varchar](200) NULL,
# [GiftInfo] [varchar](100) NULL,
# [GiftValue] [money] NULL,
# [GiftValueText] [varchar](50) NULL,
# [Dupe] [char](1) NULL
# ) ON [PRIMARY]

###########################################################

class Honoraria(models.Model):
	ID = models.CharField(max_length=15, primary_key=True)
	Chamber = models.CharField(max_length=1, default=None)
	CID = models.CharField(max_length=9, default=None)
	CalendarYear = models.CharField(max_length=2, default=None)
	ReportType = models.CharField(max_length=1, default=None)
	HonorariaSource = models.CharField(max_length=120, default=None)
	Orgname = models.CharField(max_length=60, default=None)
	Ultorg = models.CharField(max_length=60, default=None)
	Realcode = models.CharField(max_length=20, default=None)
	Source = models.CharField(max_length=20, default=None)
	HonorariaSourceLoc = models.CharField(max_length=70, default=None)
	HonorariaActivity = models.CharField(max_length=300, default=None)
	HonorariaDate = models.CharField(max_length=20, default=None)
	HonorariaDateText = models.CharField(max_length=30, default=None)
	HonorariaAmt = models.CharField(max_length=20, default=None)
	HonorariaAmtText = models.CharField(max_length=30, default=None)
	Dupe = models.CharField(max_length=1, default=None)


	def __str__(self):
		obj_str = 'ID: ' + self.ID 
		return obj_str

# CREATE TABLE [dbo].[Honoraria](
# [ID] [varchar](15) NOT NULL,
# [Chamber] [char](1) NULL,
# [CID] [char](9) NULL,
# [CalendarYear] [char](2) NULL,
# [ReportType] [char](1) NULL,
# [HonorariaSource] [varchar](100) NULL,
# [Orgname] [varchar](40) NULL,
# [Ultorg] [varchar](40) NULL,
# [Realcode] [char](5) NULL,
# [Source] [char](5) NULL,
# [HonorariaSourceLoc] [varchar](50) NULL,
# [HonorariaActivity] [varchar](255) NULL,
# [HonorariaDate] [smalldatetime] NULL,
# [HonorariaDateText] [varchar](20) NULL,
# [HonorariaAmt] [money] NULL,
# [HonorariaAmtText] [varchar](25) NULL,
# [Dupe] [char](1) NULL

##########################################################

class Income(models.Model):
	ID = models.CharField(max_length=15, primary_key=True)
	Chamber = models.CharField(max_length=1, default=None)
	CID = models.CharField(max_length=9, default=None)
	CalendarYear = models.CharField(max_length=2, default=None)
	ReportType = models.CharField(max_length=1, default=None)
	IncomeSource = models.CharField(max_length=120, default=None)
	Orgname = models.CharField(max_length=60, default=None)
	Ultorg = models.CharField(max_length=60, default=None)
	Realcode = models.CharField(max_length=20, default=None)
	Source = models.CharField(max_length=20, default=None)
	IncomeLocation = models.CharField(max_length=70, default=None)
	IncomeSpouseDep = models.CharField(max_length=1, default=None)
	IncomeType = models.CharField(max_length=70, default=None)
	IncomeAmt = models.CharField(max_length=20, default=None)
	IncomeAmtText = models.CharField(max_length=70, default=None)
	Dupe = models.CharField(max_length=1, default=None)


	def __str__(self):
		obj_str = 'ID: ' + self.ID 
		return obj_str

# CREATE TABLE [dbo].[Income](
# [ID] [varchar](15) NOT NULL,
# [Chamber] [char](1) NULL,
# [CID] [char](9) NULL,
# [CalendarYear] [char](2) NULL,
# [ReportType] [char](1) NULL,
# [IncomeSource] [nvarchar](100) NULL,
# [Orgname] [varchar](40) NULL,
# [Ultorg] [varchar](40) NULL,
# 6/14/2015 58 of 62
# [Realcode] [char](5) NULL,
# [Source] [char](5) NULL,
# [IncomeLocation] [varchar](50) NULL,
# [IncomeSpouseDep] [char](1) NULL,
# [IncomeType] [varchar](50) NULL,
# [IncomeAmt] [money] NULL,
# [IncomeAmtText] [varchar](50) NULL,
# [Dupe] [char](1) NULL
# ) ON [PRIMARY]
#####################################################

class Liability(models.Model):
	ID = models.CharField(max_length=15, primary_key=True)
	Chamber = models.CharField(max_length=1, default=None)
	CID = models.CharField(max_length=9, default=None)
	CalendarYear = models.CharField(max_length=2, default=None)
	ReportType = models.CharField(max_length=1, default=None)
	LiabilitySpouseJointDep = models.CharField(max_length=1, default=None)
	Creditor = models.CharField(max_length=120, default=None)
	Orgname = models.CharField(max_length=60, default=None)
	Ultorg = models.CharField(max_length=60, default=None)
	Realcode = models.CharField(max_length=10, default=None)
	Source = models.CharField(max_length=10, default=None)
	TypeofLiability = models.CharField(max_length=120, default=None)
	LiabilityLoc = models.CharField(max_length=70, default=None)
	LiabilityDate = models.CharField(max_length=20, default=None)
	LiabilityDateText = models.CharField(max_length=50, default=None)
	LiabilityTerm = models.CharField(max_length=70, default=None)
	LiabilityInterestRate = models.CharField(max_length=70, default=None)
	LiabilityAmt = models.CharField(max_length=5, default=None)
	Dupe = models.CharField(max_length=1, default=None)


	def __str__(self):
		obj_str = 'ID: ' + self.ID 
		return obj_str

# CREATE TABLE [dbo].[Liability](
# [ID] [varchar](15) NOT NULL,
# [Chamber] [char](1) NULL,
# [CID] [char](9) NULL,
# [CalendarYear] [char](2) NULL,
# [ReportType] [char](1) NULL,
# [LiabilitySpouseJointDep] [char](1) NULL,
# [Creditor] [varchar](100) NULL,
# [Orgname] [varchar](40) NULL,
# [Ultorg] [varchar](40) NULL,
# [Realcode] [char](5) NULL,
# [Source] [char](5) NULL,
# [TypeofLiability] [varchar](100) NULL,
# [LiabilityLoc] [varchar](50) NULL,
# [LiabilityDate] [smalldatetime] NULL,
# [LiabilityDateText] [varchar](25) NULL,
# [LiabilityTerm] [varchar](50) NULL,
# [LiabilityInterestRate] [varchar](20) NULL,
# [LiabilityAmt] [char](2) NULL,
# [Dupe] [char](1) NULL

#################################################################

class Position(models.Model):
	ID = models.CharField(max_length=15, primary_key=True)
	Chamber = models.CharField(max_length=1, default=None)
	CID = models.CharField(max_length=9, default=None)
	CalendarYear = models.CharField(max_length=2, default=None)
	ReportType = models.CharField(max_length=1, default=None)
	PreviousPositions = models.CharField(max_length=300, default=None)
	PositionHeld = models.CharField(max_length=150, default=None)
	PositionOrg = models.CharField(max_length=150, default=None)
	Orgname = models.CharField(max_length=60, default=None)
	Ultorg = models.CharField(max_length=60, default=None)
	Realcode = models.CharField(max_length=10, default=None)
	Source = models.CharField(max_length=10, default=None)
	PositionOrgLoc = models.CharField(max_length=70, default=None)
	PositionOrgType = models.CharField(max_length=70, default=None)
	PositionFromDate = models.CharField(max_length=20, default=None)
	PositionFromDateText = models.CharField(max_length=70, default=None)
	PositionToDate = models.CharField(max_length=20, default=None)
	PositionToDateText = models.CharField(max_length=70, default=None)
	Dupe = models.CharField(max_length=1, default=None)


	def __str__(self):
		obj_str = 'ID: ' + self.ID 
		return obj_str

# CREATE TABLE [dbo].[Position](
# [ID] [varchar](15) NOT NULL,
# [Chamber] [char](1) NULL,
# [CID] [char](9) NULL,
# [CalendarYear] [char](2) NULL,
# [ReportType] [char](1) NULL,
# [PreviousPositions] [varchar](255) NULL,
# [PositionHeld] [varchar](100) NULL,
# [PositionOrg] [varchar](100) NULL,
# [Orgname] [varchar](40) NULL,
# [Ultorg] [varchar](40) NULL,
# [Realcode] [char](5) NULL,
# [Source] [char](5) NULL,
# [PositionOrgLoc] [varchar](50) NULL,
# [PositionOrgType] [varchar](50) NULL,
# [PositionFromDate] [smalldatetime] NULL,
# [PositionFromDateText] [varchar](50) NULL,
# [PositionToDate] [smalldatetime] NULL,
# [PositionToDateText] [varchar](50) NULL,
# [Dupe] [char](1) NULL

#############################################

class Transaction(models.Model):
	ID = models.CharField(max_length=15, primary_key=True)
	Chamber = models.CharField(max_length=1, default=None)
	CID = models.CharField(max_length=9, default=None)
	CalendarYear = models.CharField(max_length=2, default=None)
	ReportType = models.CharField(max_length=1, default=None)
	Asset4SJD = models.CharField(max_length=1, default=None)
	Asset4Transacted = models.CharField(max_length=120, default=None)
	Orgname = models.CharField(max_length=60, default=None)
	Ultorg = models.CharField(max_length=60, default=None)
	Realcode = models.CharField(max_length=10, default=None)
	Source = models.CharField(max_length=10, default=None)
	Asset4Descrip = models.CharField(max_length=120, default=None)
	Orgname2 = models.CharField(max_length=60, default=None)
	Ultorg2 = models.CharField(max_length=60, default=None)
	Realcode2 = models.CharField(max_length=10, default=None)
	Source2 = models.CharField(max_length=10, default=None)
	Asset4Purchased = models.CharField(max_length=1, default=None)
	Asset4Sold = models.CharField(max_length=1, default=None)
	Asset4Exchanged = models.CharField(max_length=1, default=None)
	Asset4Date = models.CharField(max_length=20, default=None)
	Asset4DateText = models.CharField(max_length=70, default=None)
	Asset4TransAmt = models.CharField(max_length=5, default=None)
	Asset4ExactAmt = models.CharField(max_length=30, default=None)
	CofD = models.CharField(max_length=1, default=None)
	TransNotes = models.CharField(max_length=120, default=None)
	Dupe = models.CharField(max_length=1, default=None)


	def __str__(self):
		obj_str = 'ID: ' + self.ID 
		return obj_str

# CREATE TABLE [dbo].[Transactions](
# [ID] [varchar](15) NOT NULL,
# [Chamber] [char](1) NULL,
# [CID] [char](9) NULL,
# [CalendarYear] [char](2) NOT NULL,
# [ReportType] [char](1) NULL,
# [Asset4SJD] [char](1) NULL,
# [Asset4Transacted] [varchar](100) NULL,
# [Orgname] [varchar](40) NULL,
# [Ultorg] [varchar](40) NULL,
# [Realcode] [char](5) NULL,
# [Source] [char](5) NULL,
# [Asset4Descrip] [varchar](100) NULL,
# [Orgname2] [varchar](40) NULL,
# [Ultorg2] [varchar](40) NULL,
# [Realcode2] [char](5) NULL,
# [Source2] [char](5) NULL,
# [Asset4Purchased] [char](1) NULL,
# [Asset4Sold] [char](1) NULL,
# [Asset4Exchanged] [char](1) NULL,
# [Asset4Date] [smalldatetime] NULL,
# [Asset4DateText] [varchar](50) NULL,
# [Asset4TransAmt] [char](2) NULL,
# [Asset4ExactAmt] [decimal](18, 0) NULL,
# [CofD] [char](1) NULL,
# [TransNotes] [varchar](100) NULL,
# [Dupe] [char](1) NULL
# ) ON [PRIMARY]
#############################################

class Travel(models.Model):
	ID = models.CharField(max_length=15, primary_key=True)
	Chamber = models.CharField(max_length=1, default=None)
	CID = models.CharField(max_length=9, default=None)
	CalendarYear = models.CharField(max_length=2, default=None)
	ReportType = models.CharField(max_length=1, default=None)
	TravelSource = models.CharField(max_length=120, default=None)
	Orgname = models.CharField(max_length=60, default=None)
	Ultorg = models.CharField(max_length=60, default=None)
	Realcode = models.CharField(max_length=10, default=None)
	Source = models.CharField(max_length=10, default=None)
	SourceCity = models.CharField(max_length=70, default=None)
	SourceState = models.CharField(max_length=10, default=None)
	BeginDate = models.CharField(max_length=20, default=None)
	BeginDateText = models.CharField(max_length=50, default=None)
	EndDate = models.CharField(max_length=20, default=None)
	EndDateText = models.CharField(max_length=50, default=None)
	DepartCity = models.CharField(max_length=70, default=None)
	DepartState = models.CharField(max_length=10, default=None)
	DestCity = models.CharField(max_length=70, default=None)
	DestState = models.CharField(max_length=10, default=None)
	PofRCity = models.CharField(max_length=70, default=None)
	PofRState = models.CharField(max_length=10, default=None)
	Descrip = models.CharField(max_length=300, default=None)
	Lodging = models.CharField(max_length=1, default=None)
	Food = models.CharField(max_length=1, default=None)
	FamilyIncl = models.CharField(max_length=1, default=None)
	TimeAtOwnExpense = models.CharField(max_length=50, default=None)
	Dupe = models.CharField(max_length=1, default=None)


	def __str__(self):
		obj_str = 'ID: ' + self.ID 
		return obj_str

# CREATE TABLE [dbo].[Travel](
# [ID] [varchar](15) NOT NULL,
# [Chamber] [char](1) NULL,
# [CID] [char](9) NULL,
# [CalendarYear] [char](2) NULL,
# [ReportType] [char](1) NULL,
# [TravelSource] [varchar](100) NULL,
# [Orgname] [varchar](40) NULL,
# 6/14/2015 60 of 62
# [Ultorg] [varchar](40) NULL,
# [Realcode] [char](5) NULL,
# [Source] [char](5) NULL,
# [SourceCity] [varchar](50) NULL,
# [SourceState] [varchar](2) NULL,
# [BeginDate] [smalldatetime] NULL,
# [BeginDateText] [varchar](25) NULL,
# [EndDate] [smalldatetime] NULL,
# [EndDateText] [varchar](25) NULL,
# [DepartCity] [varchar](50) NULL,
# [DepartState] [char](2) NULL,
# [DestCity] [varchar](50) NULL,
# [DestState] [char](2) NULL,
# [PofRCity] [varchar](50) NULL,
# [PofRState] [char](2) NULL,
# [Descrip] [varchar](255) NULL,
# [Lodging] [char](1) NULL,
# [Food] [char](1) NULL,
# [FamilyIncl] [char](1) NULL,
# [TimeAtOwnExpense] [varchar](25) NULL,
# [Dupe] [char](1) NULL

###################################

class Honoraria(models.Model):
	ID = models.CharField(max_length=15, primary_key=True)
	Chamber = models.CharField(max_length=1, default=None)
	CID = models.CharField(max_length=9, default=None)
	CalendarYear = models.CharField(max_length=2, default=None)
	ReportType = models.CharField(max_length=1, default=None)
	HonorariaSource = models.CharField(max_length=120, default=None)
	Orgname = models.CharField(max_length=60, default=None)
	Ultorg = models.CharField(max_length=60, default=None)
	Realcode = models.CharField(max_length=10, default=None)
	Source = models.CharField(max_length=10, default=None)
	HonorariaSourceLoc = models.CharField(max_length=70, default=None)
	HonorariaActivity = models.CharField(max_length=300, default=None)
	HonorariaDate = models.CharField(max_length=20, default=None)
	HonorariaDateText = models.CharField(max_length=40, default=None)
	HonorariaAmt = models.CharField(max_length=20, default=None)
	HonorariaAmtText = models.CharField(max_length=50, default=None)
	Dupe = models.CharField(max_length=1, default=None)


	def __str__(self):
		obj_str = 'ID: ' + self.ID 
		return obj_str

# CREATE TABLE [dbo].[Honoraria](
# [ID] [varchar](15) NOT NULL,
# [Chamber] [char](1) NULL,
# [CID] [char](9) NULL,
# [CalendarYear] [char](2) NULL,
# [ReportType] [char](1) NULL,
# [HonorariaSource] [varchar](100) NULL,
# [Orgname] [varchar](40) NULL,
# [Ultorg] [varchar](40) NULL,
# [Realcode] [char](5) NULL,
# [Source] [char](5) NULL,
# [HonorariaSourceLoc] [varchar](50) NULL,
# [HonorariaActivity] [varchar](255) NULL,
# [HonorariaDate] [smalldatetime] NULL,
# [HonorariaDateText] [varchar](20) NULL,
# [HonorariaAmt] [money] NULL,
# [HonorariaAmtText] [varchar](25) NULL,
# [Dupe] [char](1) NULL
# ) ON [PRIMARY]

