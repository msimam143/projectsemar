# Generated by Django 4.1.4 on 2023-01-01 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='isi',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]