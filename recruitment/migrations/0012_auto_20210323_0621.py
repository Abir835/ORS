# Generated by Django 3.1.7 on 2021-03-23 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0011_auto_20210323_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writtenansdb',
            name='definition',
            field=models.TextField(default=None, max_length=500, null=True),
        ),
    ]