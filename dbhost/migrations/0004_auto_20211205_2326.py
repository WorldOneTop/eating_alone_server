# Generated by Django 2.2.7 on 2021-12-05 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbhost', '0003_review_house_id_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='house_id_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbhost.House_main'),
        ),
    ]