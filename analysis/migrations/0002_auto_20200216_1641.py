# Generated by Django 3.0.3 on 2020-02-16 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compensation',
            name='Orgname',
            field=models.CharField(default=None, max_length=50),
        ),
    ]