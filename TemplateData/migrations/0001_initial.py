# Generated by Django 4.2.6 on 2024-05-15 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=1000, unique=True)),
                ('template_path', models.CharField(max_length=1000, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EntryInterviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InterviewQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('default_answertype', models.CharField(choices=[('txt', 'Text'), ('img', 'Image'), ('clr', 'color')], max_length=30, unique=True)),
                ('title_de', models.CharField(max_length=100, unique=True)),
                ('desc_de', models.CharField(max_length=1000, unique=True)),
                ('title_en', models.CharField(max_length=100, unique=True)),
                ('desc_en', models.CharField(max_length=1000, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=1000, unique=True)),
                ('questions', models.ManyToManyField(through='TemplateData.InterviewQuestions', to='TemplateData.question')),
            ],
        ),
        migrations.AddField(
            model_name='interviewquestions',
            name='interviewTemplate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TemplateData.interviewtemplate'),
        ),
        migrations.AddField(
            model_name='interviewquestions',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TemplateData.question'),
        ),
        migrations.CreateModel(
            name='EntryTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=1000, unique=True)),
                ('interviews', models.ManyToManyField(through='TemplateData.EntryInterviews', to='TemplateData.interviewtemplate')),
            ],
        ),
        migrations.AddField(
            model_name='entryinterviews',
            name='entryTemplate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TemplateData.entrytemplate'),
        ),
        migrations.AddField(
            model_name='entryinterviews',
            name='interviewTemplate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TemplateData.interviewtemplate'),
        ),
    ]
