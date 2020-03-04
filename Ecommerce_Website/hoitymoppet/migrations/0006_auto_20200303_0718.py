# Generated by Django 2.2.10 on 2020-03-03 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoitymoppet', '0005_auto_20200303_0700'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, null=True, to='hoitymoppet.Color'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_fabric',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hoitymoppet.Fabric'),
        ),
        migrations.AlterField(
            model_name='product',
            name='style',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hoitymoppet.Styles'),
        ),
    ]
