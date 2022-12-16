from rest_framework import viewsets
from .models import Exame
from .serializers import ExameSerializer

# Create your views here.

class ExameViewSet(viewsets.ModelViewSet):
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer