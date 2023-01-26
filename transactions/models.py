from django.db import models
from uuid import uuid4

TRANSACTIONS_TYPE = [
    (1, "Débito"),
    (2, "Boleto"),
    (3, "Financiamento"),
    (4, "Crédito"),
    (5, "Recebimento Emprestimo"),
    (6, "Vendas"),
    (7, "Recebimento TED"),
    (8, "Recebimento DOC"),
    (9, "Aluguel"),
]

class Transactions(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    type = models.CharField(choices=TRANSACTIONS_TYPE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    value = models.DecimalField(max_digits=10, decimal_places=0)
    cpf = models.DecimalField(max_digits=11, decimal_places=0)
    card = models.DecimalField(max_digits=12, decimal_places=0)
    hour = models.TimeField(auto_now=False, auto_now_add=False)
    owner_store = models.CharField(max_length=14)
    name_store = models.CharField(max_length=19)
