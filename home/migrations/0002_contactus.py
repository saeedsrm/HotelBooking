# Generated by Django 3.2.14 on 2022-07-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('note', models.TextField()),
            ],
        ),
    ]
