# Generated by Django 5.1.2 on 2024-10-30 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='nationality',
            field=models.CharField(blank=True, choices=[('EUA', 'Estados Unidos'), ('BR', 'Brasil'), ('UK', 'Reino Unido')], max_length=200, null=True),
        ),
    ]