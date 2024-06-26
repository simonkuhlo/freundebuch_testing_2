# Generated by Django 5.0.6 on 2024-05-27 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserData', '0002_answer_question_entry_template_interview_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='answer',
            name='type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='interview',
            name='entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='UserData.entry'),
        ),
    ]
