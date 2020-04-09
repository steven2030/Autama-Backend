from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import *
from .models import *


# NOTE: Views connect models, serialize, and display them


# view user info
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = UserInfo.objects.all().order_by('username')
    serializer_class = UserSerializer

    # Override get_queryset and filter for only the current user.
    # uses pk, Primary Key from the DG and users id.
    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset
        if self.action == 'list':
            return self.queryset.filter(pk=self.request.user.pk)
        return self.queryset


# TODO: Add request.autama id parameter to filter results
class AutamaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = AutamaInfo.objects.all().order_by('autamaID')
    serializer_class = AutamaSerializer

    # Override get_queryset and filter for only the current Autama.
    # uses pk Primary Key from the DG and autama id.
    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(pk=self.request.user.pk)   # TODO: will user work here?
        return self.queryset


class MatchesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Matches.objects.all().order_by('userID')
    serializer_class = MatchesSerializer

    # TODO: Need to ret all userid  matches
    # Override get_queryset and filter for only the current user's matches.
    # uses pk Primary Key from the DG and autama id.
    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(userID=self.request.user.pk)  # maybe use get_user_model here instead
        return self.queryset


# TODO: add request autama id parameter to filter results
class MessagesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Messages.objects.all().order_by('timeStamp')
    serializer_class = MessagesSerializer
