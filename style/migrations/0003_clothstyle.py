# Generated by Django 5.1.2 on 2024-11-05 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('style', '0002_style_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='clothstyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('style', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
            ],
        ),
    ]
