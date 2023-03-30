# Generated by Django 4.1.7 on 2023-03-15 18:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_alter_doctor_join_date_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 16, 0, 16, 14, 326811)),
        ),
        migrations.AlterField(
            model_name='staff',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 16, 0, 16, 14, 326811)),
        ),
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('number', models.CharField(max_length=150)),
                ('visit_date', models.DateTimeField(default=datetime.datetime(2023, 3, 16, 0, 16, 14, 326811))),
                ('issue_date', models.DateTimeField(default=datetime.datetime(2023, 3, 16, 0, 16, 14, 326811))),
                ('paid', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('waiting_status', models.BooleanField(default=False)),
                ('submit_status', models.BooleanField(default=False)),
                ('done_status', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
            ],
        ),
    ]
