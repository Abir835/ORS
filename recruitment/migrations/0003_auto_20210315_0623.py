# Generated by Django 3.1.7 on 2021-03-15 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0002_auto_20210315_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancydb',
            name='vId',
            field=models.IntegerField(blank=None, null=True),
        ),
        migrations.AlterField(
            model_name='qdetail',
            name='JobPID',
            field=models.IntegerField(blank=None, null=True),
        ),
        migrations.AlterField(
            model_name='vacancydb',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vacancydetailsdb',
            name='vacancyNum',
            field=models.IntegerField(blank=None, null=True),
        ),
    ]