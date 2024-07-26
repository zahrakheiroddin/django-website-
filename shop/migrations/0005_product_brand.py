# Generated by Django 3.1.3 on 2020-12-02 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.brand'),
            preserve_default=False,
        ),
    ]
