# Generated by Django 4.1.5 on 2023-01-26 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_alter_transactions_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='type',
            field=models.CharField(choices=[('Débito', 1), ('Boleto', 2), ('Financiamento', 3), ('Crédito', 4), ('Recebimento Emprestimo', 5), ('Vendas', 6), ('Recebimento TED', 7), ('Recebimento DOC', 8), ('Aluguel', 9)], max_length=25),
        ),
    ]
