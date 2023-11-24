# Generated by Django 4.2.7 on 2023-11-23 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_padaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
    ]
