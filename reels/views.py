from rest_framework import viewsets
from .models import Reel
from .serializers import ReelSerializer

class ReelViewSet(viewsets.ModelViewSet):
    queryset = Reel.objects.all()
    serializer_class = ReelSerializer
