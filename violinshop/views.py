
from rest_framework import generics
from .models import Violin
from .serializers import ViolinSerializer


class ViolinListCreate(generics.ListCreateAPIView):
    queryset = Violin.objects.all()
    serializer_class = ViolinSerializer

