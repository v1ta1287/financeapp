# Generated by Django 4.0 on 2021-12-16 08:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_task_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='task',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 16, 8, 37, 6, 312874, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]