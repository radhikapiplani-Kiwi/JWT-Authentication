# Generated by Django 4.1.6 on 2023-02-14 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('password2', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
    ]
