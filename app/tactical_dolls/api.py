from rest_framework.generics import ListAPIView

from .serializer import DollSerializer
from .models import Doll


class Dolls(ListAPIView):
    queryset = Doll.objects.filter(type='sg')
    serializer_class = DollSerializer
