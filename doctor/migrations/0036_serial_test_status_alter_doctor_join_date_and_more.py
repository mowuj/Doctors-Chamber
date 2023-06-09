# Generated by Django 4.1.7 on 2023-03-21 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0035_test_done_status_test_pending_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serial',
            name='test_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 21, 15, 34, 26, 746538)),
        ),
        migrations.AlterField(
            model_name='serial',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 21, 15, 34, 26, 750538)),
        ),
        migrations.AlterField(
            model_name='serial',
            name='visit_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 21, 15, 34, 26, 750538)),
        ),
        migrations.AlterField(
            model_name='staff',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 21, 15, 34, 26, 750538)),
        ),
    ]
