# Generated by Django 3.2.7 on 2021-10-13 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_order_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='category',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
            preserve_default=False,
        ),
    ]
