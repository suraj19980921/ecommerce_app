# Generated by Django 3.2.7 on 2021-10-06 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20211006_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_item', to='main.shop'),
        ),
    ]
