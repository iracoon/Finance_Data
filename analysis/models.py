from django.db import models

# Create your models here.

class Compensation(models.Model):
	ID = models.CharField(max_length=15, primary_key=True)
	Chamber = models.CharField(max_length=1, default=None)
	CID = models.CharField(max_length=9, default=None)
	CalendarYear = models.CharField(max_length=2, default=None)
	ReportType = models.CharField(max_length=1, default=None)
	CompSource = models.CharField(max_length=100, default=None)
	Orgname = models.CharField(max_length=40, default=None)
	Ultorg = models.CharField(max_length=40, default=None)
	Realcode = models.CharField(max_length=5, default=None)
	Source = models.CharField(max_length=5, default=None)
	CompSourceLocation = models.CharField(max_length=50, default=None)
	CompDuties = models.CharField(max_length=100, default=None)
	dupe = models.CharField(max_length=1,default=None)

	
	def __str__(self):
		return self.title

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