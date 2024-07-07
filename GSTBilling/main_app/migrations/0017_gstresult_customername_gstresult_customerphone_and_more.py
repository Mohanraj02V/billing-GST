# Generated by Django 5.0.6 on 2024-06-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_gstresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='gstresult',
            name='customerName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='gstresult',
            name='customerPhone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gstresult',
            name='storeName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='gstresult',
            name='storeNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
