# Generated by Django 3.2.9 on 2022-07-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=20)),
                ('bill_no', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=200)),
                ('in_out', models.CharField(choices=[('In', 'In'), ('Out', 'Out')], max_length=5, verbose_name='In/Out')),
                ('amount', models.FloatField()),
                ('comment', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
