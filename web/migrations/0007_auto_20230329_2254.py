# Generated by Django 3.2 on 2023-03-30 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_pedido_pedidodetalle'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='codigo_pago',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='forma_pago',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
