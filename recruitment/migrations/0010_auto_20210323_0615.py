# Generated by Django 3.1.7 on 2021-03-23 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0009_auto_20210323_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writtenansdb',
            name='definition',
            field=models.TextField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='writtenansdb',
            name='iqTest',
            field=models.TextField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='writtenansdb',
            name='math1',
            field=models.TextField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='writtenansdb',
            name='math2',
            field=models.TextField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='writtenansdb',
            name='math3',
            field=models.TextField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='writtenansdb',
            name='syntax1',
            field=models.TextField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='writtenansdb',
            name='syntax2',
            field=models.TextField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='writtenansdb',
            name='syntax3',
            field=models.TextField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='writtenansdb',
            name='syntax4',
            field=models.TextField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='writtenansdb',
            name='theory',
            field=models.TextField(default=None, max_length=500, null=True),
        ),
    ]
