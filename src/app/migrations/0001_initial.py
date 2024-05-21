# Generated by Django 5.0.6 on 2024-05-21 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('attr', models.CharField(blank=True, max_length=255, null=True)),
                ('sport_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sport.sporttype')),
            ],
            options={
                'verbose_name': 'Competition',
                'verbose_name_plural': 'Competitions',
                'db_table': 'competition',
            },
        ),
    ]