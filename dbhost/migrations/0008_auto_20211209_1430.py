# Generated by Django 2.2.7 on 2021-12-09 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbhost', '0007_auto_20211209_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='body',
            field=models.TextField(),
        ),
    ]
