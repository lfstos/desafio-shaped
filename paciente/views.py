from rest_framework import viewsets
from .models import Paciente
from .serializers import PacienteSerializer

# Create your views here.
class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer