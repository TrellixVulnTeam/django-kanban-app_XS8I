# Generated by Django 3.1.4 on 2021-01-17 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210117_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pbi',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.departments'),
        ),
    ]
