# Generated by Django 3.0.6 on 2020-05-12 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='sku',
            new_name='p_id',
        ),
    ]