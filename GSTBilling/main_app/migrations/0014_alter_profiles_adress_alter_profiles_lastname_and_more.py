# Generated by Django 5.0.6 on 2024-06-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_alter_profiles_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='adress',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='lastname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='phonenumber',
            field=models.CharField(max_length=15),
        ),
    ]
