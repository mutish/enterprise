# Generated by Django 4.0.2 on 2023-03-17 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adminshoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoesname', models.CharField(db_column='shoesname', max_length=100)),
                ('shoesimage', models.URLField(db_column='shoesimage')),
                ('shoesprice', models.CharField(db_column='shoesprice', max_length=100)),
            ],
            options={
                'verbose_name': 'Adminshoe',
                'verbose_name_plural': 'Adminshoes',
                'db_table': 'adminshoe',
            },
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactionID', models.CharField(db_column='transactionID', max_length=100)),
                ('amount', models.CharField(db_column='amount', max_length=100)),
                ('phone', models.CharField(db_column='phone', max_length=100)),
            ],
            options={
                'verbose_name': 'Checkout',
                'verbose_name_plural': 'Checkouts',
                'db_table': 'checkout',
            },
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoes_name', models.CharField(max_length=100)),
                ('shoes_image', models.URLField()),
                ('shoes_price', models.CharField(max_length=10000000)),
            ],
            options={
                'db_table': 'shoes',
            },
        ),
    ]
