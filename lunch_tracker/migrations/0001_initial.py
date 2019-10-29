# Generated by Django 2.2.4 on 2019-10-28 02:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('account_number', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(max_length=50)),
                ('allergens', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cust_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_choice', to='lunch_tracker.Customer')),
                ('meal_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='lunch_tracker.Customer')),
                ('meal_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_choice', to='lunch_tracker.Meal')),
            ],
        ),
    ]