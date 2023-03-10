# Generated by Django 4.1.4 on 2023-01-02 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_rename_tamggal_artikel_tanggal'),
    ]

    operations = [
        migrations.CreateModel(
            name='komen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateTimeField(auto_now_add=True, null=True)),
                ('isi', models.TextField(blank=True, max_length=500, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('artikel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.artikel')),
            ],
        ),
    ]
