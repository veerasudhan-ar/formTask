# Generated by Django 4.0.4 on 2022-05-10 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formTaskApp', '0002_alter_basicform_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicform',
            name='address',
            field=models.CharField(blank=True, max_length=128, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='basicform',
            name='age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='basicform',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='basicform',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
