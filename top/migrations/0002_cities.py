# Generated by Django 3.2.3 on 2021-06-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
