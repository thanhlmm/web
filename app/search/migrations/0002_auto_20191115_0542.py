# Generated by Django 2.2.3 on 2019-11-15 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchresult',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
