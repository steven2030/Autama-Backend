from rest_framework import serializers
from .models import User
from .models import AutamaProfile
# TODO: Do we need to separate from individual messages and history?
from .models import Messages


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # TODO: Is this a valid concern?
        # Not passing user ID to prevent return from being modified
        fields = ['username', 'first_name', 'last_name', 'email', 'sex', 'interest1',
                  'interest2', 'interest3', 'interest4', 'interest5']


class AutamaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AutamaProfile
        fields = ['creator', 'picture', 'first', 'last', 'nummatches', 'owner',
                  'interest1', 'interest2', 'interest3']


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Messages
        fields = ['sender', 'timeStamp', 'message']
