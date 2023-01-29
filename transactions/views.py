from rest_framework.generics import ListCreateAPIView
from .models import Transactions
from .serializers import TransactionSerializer

class TransactionView(ListCreateAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer