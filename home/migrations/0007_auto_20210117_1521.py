# Generated by Django 3.1.4 on 2021-01-17 12:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_pbi_department_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='department_adress',
            field=models.CharField(default=django.utils.timezone.now, max_length=150, verbose_name='Departman adress:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='departments',
            name='department_mail',
            field=models.CharField(default=django.utils.timezone.now, max_length=150, verbose_name='Departman Mail:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pbi',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='home.departments', verbose_name='Departman'),
        ),
    ]