# Generated by Django 3.2.6 on 2021-08-18 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_member_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ('created_at',)},
        ),
    ]
