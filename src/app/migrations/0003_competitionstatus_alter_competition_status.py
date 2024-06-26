# Generated by Django 5.0 on 2024-05-28 04:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_applicationstatus_competition_user_agecategory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetitionStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('attr', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Competition Status',
                'verbose_name_plural': 'Competition Statuses',
                'db_table': 'competition_status',
            },
        ),
        migrations.AlterField(
            model_name='competition',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.competitionstatus'),
        ),
    ]
