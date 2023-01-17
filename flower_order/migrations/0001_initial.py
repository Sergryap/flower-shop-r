# Generated by Django 4.1.5 on 2023-01-17 20:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bouquet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, unique=True, verbose_name='Название')),
                ('price', models.PositiveSmallIntegerField(default=1600, verbose_name='Цена')),
                ('image', models.FileField(blank=True, null=True, upload_to='images/bouquets', validators=[django.core.validators.FileExtensionValidator(['png', 'jpeg', 'svg'])], verbose_name='Изображение')),
                ('discription', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('structure', models.TextField(blank=True, null=True, verbose_name='Состав')),
                ('height', models.PositiveSmallIntegerField(default=30, verbose_name='Высота')),
                ('width', models.PositiveSmallIntegerField(default=20, verbose_name='Ширина')),
            ],
            options={
                'verbose_name': 'букет',
                'verbose_name_plural': 'букеты',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=128, region=None, verbose_name='Телефон')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, max_length=200, null=True, verbose_name='Фамилия')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=128, region='RU', unique=True, verbose_name='Телефон')),
                ('address', models.CharField(db_index=True, max_length=200, unique=True, verbose_name='Адрес')),
                ('image', models.FileField(blank=True, null=True, upload_to='images/shops', validators=[django.core.validators.FileExtensionValidator(['png', 'jpeg', 'svg'])], verbose_name='Изображение')),
                ('latitude', models.DecimalField(decimal_places=6, default=59.940722, max_digits=8, verbose_name='Широта')),
                ('longitude', models.DecimalField(decimal_places=6, default=30.396429, max_digits=8, verbose_name='Долгота')),
            ],
            options={
                'verbose_name': 'магазин',
                'verbose_name_plural': 'магазины',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=128, region='RU', unique=True, verbose_name='Телефон')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('surname', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('position', models.CharField(choices=[('master', 'Мастер'), ('courier', 'Курьер')], max_length=200, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'сотрудник',
                'verbose_name_plural': 'сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(blank=True, choices=[('consultation', 'Консультация'), ('delivery', 'Доставка')], max_length=15, null=True, verbose_name='Статус')),
                ('status', models.CharField(choices=[('1 not processed', 'Необработан'), ('2 collect', 'Собирается'), ('3 on way', 'В пути'), ('4 completed', 'Выполнен')], db_index=True, default='1 not processed', max_length=15, verbose_name='Статус')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес доставки')),
                ('bouquets', models.ManyToManyField(related_name='orders', to='flower_order.bouquet', verbose_name='Букеты')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='flower_order.client', verbose_name='Клиент')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='flower_order.staff', verbose_name='сотрудник')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
            },
        ),
        migrations.AddField(
            model_name='bouquet',
            name='categories',
            field=models.ManyToManyField(related_name='bouquets', to='flower_order.category', verbose_name='Категории'),
        ),
    ]
