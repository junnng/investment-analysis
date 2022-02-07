# Generated by Django 4.0.2 on 2022-02-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(null=True)),
                ('stock_code', models.CharField(max_length=200, null=True)),
                ('stock_name', models.CharField(max_length=200, null=True, unique=True)),
                ('market', models.CharField(default='', max_length=200, null=True)),
                ('sector', models.CharField(default='', max_length=200, null=True)),
                ('industry', models.CharField(default='', max_length=200, null=True)),
                ('listing_date', models.CharField(default='', max_length=200, null=True)),
                ('settle_month', models.CharField(default='', max_length=200, null=True)),
                ('representative', models.CharField(default='', max_length=200, null=True)),
                ('homepage', models.CharField(default='', max_length=200, null=True)),
                ('region', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rnn_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(null=True)),
                ('user_id', models.CharField(max_length=200, null=True)),
                ('stock_code', models.CharField(max_length=200)),
                ('stock_name', models.CharField(max_length=200)),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Rnn_result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(null=True)),
                ('user_id', models.CharField(max_length=200, null=True)),
                ('stock_code', models.CharField(max_length=200)),
                ('stock_name', models.CharField(max_length=200)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('result_max', models.DecimalField(decimal_places=2, max_digits=10)),
                ('result_min', models.DecimalField(decimal_places=2, max_digits=10)),
                ('d1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('d2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('d3', models.DecimalField(decimal_places=2, max_digits=10)),
                ('d4', models.DecimalField(decimal_places=2, max_digits=10)),
                ('d5', models.DecimalField(decimal_places=2, max_digits=10)),
                ('d6', models.DecimalField(decimal_places=2, max_digits=10)),
                ('d7', models.DecimalField(decimal_places=2, max_digits=10)),
                ('train_RMSE', models.DecimalField(decimal_places=2, max_digits=10)),
                ('test_RMSE', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(null=True)),
                ('stock_code', models.CharField(max_length=200)),
                ('stock_name', models.CharField(max_length=200)),
            ],
        ),
    ]
