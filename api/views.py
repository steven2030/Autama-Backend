from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *


# NOTE: Views connect models, serialize, and display them

# view users
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer

    # alternative? User.objects.filter(pk)
    # Override get_queryset and filter for only the current user.
    # uses pk Primary Key from the DG and users id.
    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(pk=self.request.user.pk)
        return self.queryset


# TODO: Add request.autama id parameter to filter results
class AutamaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = AutamaProfile.objects.all().order_by('autamaID')
    serializer_class = AutamaSerializer


# TODO: Add filters if needed
class MatchViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Matches.objects.all().order_by('userID')
    serializer_class = MatchesSerializer


# TODO: add request autama id parameter to filter results
class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Messages.objects.all().order_by('timeStamp')
    serializer_class = MessageSerializer
