# Generated by Django 2.2.7 on 2021-12-09 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbhost', '0012_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]