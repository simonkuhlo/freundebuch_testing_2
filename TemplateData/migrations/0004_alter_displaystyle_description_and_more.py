# Generated by Django 5.0.6 on 2024-06-07 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TemplateData', '0003_alter_question_default_answertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='displaystyle',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='displaystyle',
            name='template_path',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='entrytemplate',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='interviewtemplate',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='question',
            name='default_answertype',
            field=models.CharField(choices=[('text', 'Text'), ('image', 'Image'), ('color', 'color')], max_length=30),
        ),
        migrations.AlterField(
            model_name='question',
            name='desc_de',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='question',
            name='desc_en',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='question',
            name='title_de',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='title_en',
            field=models.CharField(max_length=100),
        ),
    ]