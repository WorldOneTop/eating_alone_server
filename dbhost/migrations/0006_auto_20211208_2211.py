# Generated by Django 2.2.7 on 2021-12-08 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbhost', '0005_auto_20211206_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
