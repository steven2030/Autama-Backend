from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer

    # Override get_queryset and filter for only the current user.
    # uses pk Primary Key from the DG and users id.
    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(pk=self.request.user.pk)
        return self.queryset


# TODO: Add request.autama id parameter to filter results
class AIViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = AutamaProfile.objects.all().order_by('autamaid')
    serializer_class = AutamaSerializer


# TODO: add request autama id parameter to filter results
class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Messages.objects.all().order_by('timeStamp')
    serializer_class = MessageSerializer
