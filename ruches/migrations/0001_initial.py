# Generated by Django 5.1.2 on 2024-10-18 01:01

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ruche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('date_inspection', models.DateField(blank=True, null=True)),
                ('niveaux_miel', models.FloatField(help_text='Niveau de miel en kg')),
                ('infestations', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('emplacement', models.CharField(max_length=200)),
                ('date_creation', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Recolte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_recolte', models.DateField()),
                ('quantite_miel', models.FloatField(help_text='Quantité de miel récolté en kg')),
                ('ruche', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recoltes', to='ruches.ruche')),
            ],
        ),
        migrations.AddField(
            model_name='ruche',
            name='rucher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ruches', to='ruches.rucher'),
        ),
        migrations.CreateModel(
            name='Reine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('sante', models.CharField(max_length=100)),
                ('date_remplacement', models.DateField()),
                ('rucher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reines', to='ruches.rucher')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('date_notification', models.DateTimeField(auto_now_add=True)),
                ('rucher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ruches.rucher')),
            ],
        ),
    ]