# Generated by Django 4.1.5 on 2023-01-08 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户数据', 'verbose_name_plural': '用户数据'},
        ),
    ]
