# Generated by Django 2.2.10 on 2020-03-04 11:54

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoitymoppet', '0009_auto_20200304_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', max_length=18),
        ),
        migrations.AlterField(
            model_name='color',
            name='parent_color',
            field=colorfield.fields.ColorField(blank=True, default='#FFFFFF', max_length=18, null=True, verbose_name='self'),
        ),
    ]
