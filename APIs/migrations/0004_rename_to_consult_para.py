# Generated by Django 4.1.4 on 2022-12-16 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APIs', '0003_rename_para_consult_to'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consult',
            old_name='to',
            new_name='para',
        ),
    ]
