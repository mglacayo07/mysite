# Generated by Django 4.1 on 2022-08-11 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_question_updated_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choise',
            new_name='Choice',
        ),
    ]
