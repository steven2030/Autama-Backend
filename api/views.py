from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    # TODO: Get this users id and return ONLY.
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer

    # queryset = User.objects.all()
    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     if pk == "current":
    #         return self.request.user



class AIViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = AutamaProfile.objects.all().order_by('autamaid')
    serializer_class = AutamaSerializer


class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Messages.objects.all().order_by('timeStamp')
    serializer_class = MessageSerializer
