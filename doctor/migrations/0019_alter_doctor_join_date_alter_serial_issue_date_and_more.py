# Generated by Django 4.1.7 on 2023-03-17 20:38

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0018_alter_announcement_user_alter_doctor_join_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 2, 38, 26, 841851)),
        ),
        migrations.AlterField(
            model_name='serial',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 2, 38, 26, 841851)),
        ),
        migrations.AlterField(
            model_name='serial',
            name='visit_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 2, 38, 26, 841851)),
        ),
        migrations.AlterField(
            model_name='staff',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 2, 38, 26, 841851)),
        ),
        migrations.CreateModel(
            name='RelatedImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('photo', models.ImageField(blank=True, default='default.jpg', upload_to='media/images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
