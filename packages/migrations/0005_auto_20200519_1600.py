# Generated by Django 3.0.6 on 2020-05-19 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0004_auto_20200514_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='event_date',
        ),
        migrations.AlterField(
            model_name='package',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
