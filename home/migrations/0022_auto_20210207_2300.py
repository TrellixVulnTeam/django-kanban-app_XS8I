# Generated by Django 3.1.4 on 2021-02-07 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20210207_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pbi',
            name='pbi',
            field=models.CharField(max_length=200, verbose_name='PBI'),
        ),
    ]
