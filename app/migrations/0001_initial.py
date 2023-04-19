# Generated by Django 4.2 on 2023-04-19 10:39

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tevekenyseg',
            fields=[
                ('tevekenyseg_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('tevekenyseg_nev', models.CharField(max_length=100, unique=True, verbose_name='Tevékenység neve')),
                ('pontszam', models.IntegerField(verbose_name='Pontszám')),
            ],
        ),
        migrations.CreateModel(
            name='Bejegyzes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osztaly_id', models.CharField(choices=[('0', 'SZF1A'), ('1', 'SZF1B'), ('2', 'SZF2'), ('3', 'nSZF1A'), ('4', 'nSZF1B')], max_length=10, verbose_name='Osztályok')),
                ('allapot', models.CharField(choices=[('Jóvahagyásra vár', 'Jóvahagyásra vár'), ('Jóváhagyott', 'Jóváhagyott')], default='Jóvahagyásra vár', max_length=50, verbose_name='Állapot')),
                ('tevekenyseg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tevekenyseg', verbose_name='Tevékenység')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='E-mail')),
                ('osztaly_id', models.CharField(choices=[('0', 'SZF1A'), ('1', 'SZF1B'), ('2', 'SZF2'), ('3', 'nSZF1A'), ('4', 'nSZF1B')], max_length=10, verbose_name='Osztály')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
