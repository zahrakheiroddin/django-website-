# Generated by Django 3.1.2 on 2020-11-02 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
