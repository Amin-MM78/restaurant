# Generated by Django 3.1.7 on 2021-03-07 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApp', '0002_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=30, verbose_name='write your email here')),
                ('subject', models.CharField(max_length=20)),
                ('message', models.TextField(max_length=300)),
            ],
        ),
    ]