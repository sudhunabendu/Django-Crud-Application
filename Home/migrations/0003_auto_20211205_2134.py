# Generated by Django 3.2.8 on 2021-12-05 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='username')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('password', models.CharField(max_length=100, verbose_name='password')),
            ],
        ),
        migrations.AlterField(
            model_name='page',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Home.user'),
        ),
    ]
