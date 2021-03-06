# Generated by Django 3.2.7 on 2021-09-11 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_cart_item_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='item_image',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='item_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='purchase_time',
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='purchase_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
