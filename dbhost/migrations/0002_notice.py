# Generated by Django 2.2.7 on 2021-12-05 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbhost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=60)),
                ('body', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
