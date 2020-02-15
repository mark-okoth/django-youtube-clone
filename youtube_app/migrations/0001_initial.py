# Generated by Django 2.2 on 2020-01-28 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('video', models.FileField(upload_to='videos/%Y/%m/%d/')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]