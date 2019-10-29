# Generated by Django 2.2.6 on 2019-10-28 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunch_tracker', '0002_auto_20191028_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
    ]