# Generated by Django 3.1.4 on 2021-01-10 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_pbi_department_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pbi',
            name='department_name',
        ),
    ]