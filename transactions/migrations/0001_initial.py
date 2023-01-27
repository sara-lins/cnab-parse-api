# Generated by Django 4.1.5 on 2023-01-26 21:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[(1, 'Débito'), (2, 'Boleto'), (3, 'Financiamento'), (4, 'Crédito'), (5, 'Recebimento Emprestimo'), (6, 'Vendas'), (7, 'Recebimento TED'), (8, 'Recebimento DOC'), (9, 'Aluguel')], max_length=25)),
                ('date', models.DateField()),
                ('value', models.DecimalField(decimal_places=0, max_digits=10)),
                ('cpf', models.DecimalField(decimal_places=0, max_digits=11)),
                ('card', models.DecimalField(decimal_places=0, max_digits=12)),
                ('hour', models.TimeField()),
                ('owner_store', models.CharField(max_length=14)),
                ('name_store', models.CharField(max_length=19)),
            ],
        ),
    ]
