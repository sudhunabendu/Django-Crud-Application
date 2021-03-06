# Generated by Django 3.2.8 on 2021-12-06 20:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_auto_20211205_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=100, verbose_name='Post_title')),
                ('description', models.TextField(verbose_name='post_description')),
                ('post_date', models.DateField(default=datetime.date.today)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.user')),
            ],
        ),
    ]
