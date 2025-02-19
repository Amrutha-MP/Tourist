# Generated by Django 5.1 on 2024-09-01 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(blank=True, max_length=50, null=True)),
                ('Package_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Package_Description', models.CharField(blank=True, max_length=50, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Days', models.CharField(blank=True, max_length=50, null=True)),
                ('Description1', models.CharField(blank=True, max_length=50, null=True)),
                ('Description2', models.CharField(blank=True, max_length=50, null=True)),
                ('Description3', models.CharField(blank=True, max_length=50, null=True)),
                ('Image1', models.ImageField(blank=True, null=True, upload_to='Package Images')),
                ('Image2', models.ImageField(blank=True, null=True, upload_to='Package Images')),
                ('Image3', models.ImageField(blank=True, null=True, upload_to='Package Images')),
            ],
        ),
    ]
