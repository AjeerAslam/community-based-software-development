# Generated by Django 4.0.6 on 2022-07-31 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expert_login', '0005_modules_md_suggestion_alter_modules_md_input_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modules',
            old_name='md_suggestion',
            new_name='md_sugg',
        ),
    ]
