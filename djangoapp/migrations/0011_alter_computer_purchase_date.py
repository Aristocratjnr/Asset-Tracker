# Generated by Django 4.2.5 on 2024-07-19 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0010_alter_operating_system_operating_system'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='purchase_date',
            field=models.DateField(blank=True, null=True, verbose_name='Purchase Date'),
        ),
    ]