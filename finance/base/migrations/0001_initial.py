# Generated by Django 4.0 on 2021-12-16 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('priority', models.IntegerField()),
                ('status', models.CharField(default='Not Done', max_length=10)),
            ],
        ),
    ]