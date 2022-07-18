# Generated by Django 4.0.5 on 2022-07-12 18:31

from django.db import migrations, models
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_inputs_inputfile_inputs_outputfile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='submission_language',
            field=models.CharField(default='cpp', max_length=5),
        ),
        migrations.AlterField(
            model_name='submission',
            name='submission_code',
            field=models.FileField(upload_to=polls.models.Submission.upload_code_name),
        ),
    ]
