# Generated by Django 4.1.7 on 2023-03-19 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0021_alter_doctor_join_date_alter_serial_issue_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serial',
            name='gender',
            field=models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE')], default='Male', max_length=150),
        ),
        migrations.AddField(
            model_name='serial',
            name='pressure',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='serial',
            name='weight',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 19, 20, 17, 48, 337050)),
        ),
        migrations.AlterField(
            model_name='serial',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 19, 20, 17, 48, 340042)),
        ),
        migrations.AlterField(
            model_name='serial',
            name='visit_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 19, 20, 17, 48, 340042)),
        ),
        migrations.AlterField(
            model_name='staff',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 19, 20, 17, 48, 339046)),
        ),
    ]
