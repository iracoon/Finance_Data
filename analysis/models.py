from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# drop tables
# delete old migration files for table if they exist
# DELETE FROM finance_data.django_migrations WHERE app='analysis';
# python ./manage.py makemigrations analysis (1)
# python ./manage.py migrate analysis (2)

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




class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('analysis-research-detail', kwargs={'pk': self.pk})