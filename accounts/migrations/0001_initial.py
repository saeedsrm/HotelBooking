# Generated by Django 3.2.6 on 2022-07-05 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('picture', models.FileField(blank=True, default='user_picture/avatar5.png', upload_to='user_picture/', verbose_name='pic')),
                ('first_name', models.CharField(blank=True, max_length=60, verbose_name='name')),
                ('last_name', models.CharField(blank=True, max_length=60, verbose_name='last name')),
                ('username', models.CharField(blank=True, max_length=60, null=True, unique=True, verbose_name='username')),
                ('phone_number', models.BigIntegerField(blank=True, default=0, null=True, verbose_name='phone')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='email')),
                ('is_active', models.BooleanField(default=True, verbose_name='isactive')),
                ('staff', models.BooleanField(default=True, verbose_name='')),
                ('isownerHotel', models.BooleanField(default=False, verbose_name='isOwnHotel')),
                ('admin', models.BooleanField(default=False, verbose_name='isadmin')),
                ('join_date', models.DateField(auto_now_add=True, verbose_name='join_date')),
            ],
            options={
                'verbose_name': 'Accounts',
                'verbose_name_plural': 'Accounts',
            },
        ),
    ]
