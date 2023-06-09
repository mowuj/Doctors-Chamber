# Generated by Django 4.1.7 on 2023-03-21 16:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0037_rename_test_status_serial_test_done_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtest',
            name='min_point',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 21, 22, 3, 54, 443995)),
        ),
        migrations.AlterField(
            model_name='serial',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 21, 22, 3, 54, 459579)),
        ),
        migrations.AlterField(
            model_name='serial',
            name='visit_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 21, 22, 3, 54, 459579)),
        ),
        migrations.AlterField(
            model_name='staff',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 21, 22, 3, 54, 443995)),
        ),
        migrations.CreateModel(
            name='TestReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.FloatField()),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.serial')),
                ('test_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.test')),
            ],
        ),
    ]
