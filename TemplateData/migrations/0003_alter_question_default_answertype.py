# Generated by Django 5.0.6 on 2024-06-07 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TemplateData', '0002_interviewtemplate_displaystyle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='default_answertype',
            field=models.CharField(choices=[('text', 'Text'), ('image', 'Image'), ('color', 'color')], max_length=30, unique=True),
        ),
    ]
