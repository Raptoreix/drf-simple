# Generated by Django 5.1.1 on 2024-09-30 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='create_at',
            new_name='created_at',
        ),
    ]