# Generated by Django 4.1.7 on 2023-03-30 15:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0045_lab_photo_alter_doctor_join_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtest',
            name='lab',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.lab'),
        ),
        migrations.AddField(
            model_name='labtest',
            name='total_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='testreport',
            name='report_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.labassistant'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 30, 21, 42, 11, 813839)),
        ),
        migrations.AlterField(
            model_name='labassistant',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 30, 21, 42, 11, 829427)),
        ),
        migrations.AlterField(
            model_name='serial',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 30, 21, 42, 11, 813839)),
        ),
        migrations.AlterField(
            model_name='serial',
            name='visit_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 30, 21, 42, 11, 813839)),
        ),
        migrations.AlterField(
            model_name='staff',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 30, 21, 42, 11, 813839)),
        ),
    ]