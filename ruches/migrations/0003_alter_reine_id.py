# Generated by Django 5.1.2 on 2024-10-19 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruches', '0002_alter_recolte_date_recolte_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reine',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]