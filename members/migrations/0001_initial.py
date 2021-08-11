# Generated by Django 3.2.6 on 2021-08-09 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programs', '0004_alter_program_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(editable=False, max_length=20, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='programs.program')),
            ],
        ),
    ]