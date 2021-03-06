# Generated by Django 3.2.7 on 2021-09-11 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_item_item_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=250)),
                ('item_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='item_price',
            field=models.FloatField(default=20),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('price', models.FloatField()),
                ('purchase_date', models.DateField(auto_now_add=True)),
                ('purchase_time', models.TimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cart')),
                ('item_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='main.item')),
                ('shop_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_item', to='main.item')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.item'),
        ),
    ]
