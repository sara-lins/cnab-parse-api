# Generated by Django 4.1.5 on 2023-01-26 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_alter_transactions_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='type',
            field=models.CharField(choices=[(1, 'Débito'), (2, 'Boleto'), (3, 'Financiamento'), (4, 'Crédito'), (5, 'Recebimento Emprestimo'), (6, 'Vendas'), (7, 'Recebimento TED'), (8, 'Recebimento DOC'), (9, 'Aluguel')], max_length=25),
        ),
    ]
