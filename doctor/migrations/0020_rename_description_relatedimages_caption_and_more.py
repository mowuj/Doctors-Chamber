# Generated by Django 4.1.7 on 2023-03-17 21:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0019_alter_doctor_join_date_alter_serial_issue_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relatedimages',
            old_name='description',
            new_name='caption',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 3, 12, 18, 844762)),
        ),
        migrations.AlterField(
            model_name='serial',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 3, 12, 18, 844762)),
        ),
        migrations.AlterField(
            model_name='serial',
            name='visit_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 3, 12, 18, 844762)),
        ),
        migrations.AlterField(
            model_name='staff',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 3, 12, 18, 844762)),
        ),
    ]
