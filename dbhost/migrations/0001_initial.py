# Generated by Django 2.2.7 on 2021-12-05 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House_main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=10)),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                ('review_count', models.PositiveSmallIntegerField(default=0)),
                ('location', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=11)),
                ('nickName', models.CharField(max_length=20)),
                ('image', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='House_detail',
            fields=[
                ('house_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dbhost.House_main')),
                ('info', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=120, null=True)),
                ('lat', models.DecimalField(decimal_places=7, max_digits=9)),
                ('lng', models.DecimalField(decimal_places=7, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('hashtag', models.CharField(max_length=200, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('user_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbhost.User')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=60)),
                ('body', models.TextField()),
                ('image', models.CharField(max_length=60)),
                ('category', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbhost.User')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('url', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('review_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbhost.Review')),
            ],
        ),
        migrations.CreateModel(
            name='House_menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('house_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbhost.House_main')),
                ('image', models.ForeignKey(db_column='url', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_image', to='dbhost.Image')),
            ],
        ),
        migrations.AddField(
            model_name='house_main',
            name='price_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='price_fk', to='dbhost.Image'),
        ),
        migrations.AddField(
            model_name='house_main',
            name='profile_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_fk', to='dbhost.Image'),
        ),
    ]