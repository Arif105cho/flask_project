# Generated by Django 4.0.2 on 2022-02-06 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppName', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]