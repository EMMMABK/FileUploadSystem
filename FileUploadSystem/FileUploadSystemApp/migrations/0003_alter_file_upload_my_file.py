# Generated by Django 5.1.5 on 2025-01-26 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FileUploadSystemApp', '0002_alter_file_upload_my_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_upload',
            name='my_file',
            field=models.FileField(upload_to=''),
        ),
    ]
