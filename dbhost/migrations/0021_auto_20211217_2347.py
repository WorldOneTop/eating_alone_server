# Generated by Django 2.2.7 on 2021-12-17 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbhost', '0020_auto_20211217_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.CharField(max_length=62, null=True),
        ),
    ]
