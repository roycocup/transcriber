# Generated by Django 3.1.7 on 2021-03-09 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcriber', '0008_uploads_hashed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploads',
            name='hashed',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
