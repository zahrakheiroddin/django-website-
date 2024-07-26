# Generated by Django 3.1.3 on 2021-09-26 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_product_wholesale_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='special',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('key', models.CharField(max_length=5)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='SpecialItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special_items', to='shop.product')),
                ('special', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shop.special')),
            ],
        ),
    ]
