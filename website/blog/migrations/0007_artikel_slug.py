# Generated by Django 4.1.4 on 2023-01-02 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_keteramgan_kategori_keterangan'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
    ]
