# Generated by Django 4.1.4 on 2023-01-01 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_artikel_isi'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='tamggal',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
