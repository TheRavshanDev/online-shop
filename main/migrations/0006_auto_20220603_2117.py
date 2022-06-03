# Generated by Django 3.2.9 on 2022-06-03 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_tovar_barcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tovar',
            name='barcode',
        ),
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_id', models.CharField(max_length=1)),
                ('manufacturer_id', models.CharField(max_length=6)),
                ('product_number', models.CharField(max_length=5)),
                ('barcode', models.ImageField(blank=True, upload_to='barcode/')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.tovar')),
            ],
        ),
    ]
