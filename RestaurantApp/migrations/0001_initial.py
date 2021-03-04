# Generated by Django 2.2.17 on 2021-03-03 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ReserveTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ReserveDateTime', models.DateTimeField()),
                ('how_many', models.SmallIntegerField(verbose_name='Number of People')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FoodName', models.CharField(max_length=30)),
                ('Description', models.TextField(max_length=300)),
                ('Size', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=2)),
                ('Price', models.IntegerField()),
                ('ImageFood', models.ImageField(upload_to='')),
                ('PreparationTime', models.SmallIntegerField()),
                ('SpecialFood', models.BooleanField(default=False)),
                ('FCategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='RestaurantApp.FoodCategory')),
            ],
        ),
    ]
