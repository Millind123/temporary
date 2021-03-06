# Generated by Django 4.0.5 on 2022-07-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_submission_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputs',
            name='inputfile',
            field=models.FileField(default='default.txt', upload_to='AllData/inputs'),
        ),
        migrations.AddField(
            model_name='inputs',
            name='outputfile',
            field=models.FileField(default='default.txt', upload_to='AllData/outputs'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='submission_code',
            field=models.FileField(upload_to='AllData/codes'),
        ),
    ]
