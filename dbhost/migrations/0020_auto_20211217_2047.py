# Generated by Django 2.2.7 on 2021-12-17 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbhost', '0019_auto_20211211_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='images',
            field=models.CharField(max_length=104, null=True),
        ),
    ]
