# Generated by Django 5.0 on 2024-05-23 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SportType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('attr', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Sport Type',
                'verbose_name_plural': 'Sport Types',
                'db_table': 'sport_type',
            },
        ),
    ]
