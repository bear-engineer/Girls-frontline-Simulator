from rest_framework.generics import ListAPIView

from .serializer import DollSerializer
from .models import Doll


class Dolls(ListAPIView):
    queryset = Doll.objects.all()
    serializer_class = DollSerializer
