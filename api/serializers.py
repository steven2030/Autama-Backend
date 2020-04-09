from rest_framework import serializers
from django.contrib.auth.models import User  # needed? are we overloading class User(below)?
from .models import User, Autama, Matches, Messages
# TODO: Do we need to separate from individual messages and history?
# from .models import Messages


# NOTE: serializers turn models into json data to send thru service

# return user object as data
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # TODO: Is this a valid concern?
        # Not passing user ID to prevent return from being modified
        # TODO: Where to Add Image?
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'gender',
                  'interest1', 'interest2', 'interest3', 'interest4', 'interest5', 'interest6']

    # Override create event to correctly encrypt password.
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender'],
            interest1=validated_data['interest1'],
            interest2=validated_data['interest2'],
            interest3=validated_data['interest3'],
            interest4=validated_data['interest4'],
            interest5=validated_data['interest5'],
            interest6=validated_data['interest6'],
        )
        return user


# return Autama object as data(json)
class AutamaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autama
        # should we also return autamaID? pickle?
        fields = ['creator', 'picture', 'first', 'last', 'num_matches', 'owner',
                  'interest1', 'interest2', 'interest3']
        # not returning interest4, interest5, interest6 for some personality intrigue/mystery
        # and do we need slug ret here?


# return Message object as data
class MessagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Messages
        fields = ['matchID', 'userID', 'autamaID', 'sender', 'timeStamp', 'messageTxt']  # ?
        # fields = ['sender', 'timeStamp', 'messageTxt']


# return list of User-Autama Matches
class MatchesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Matches
        # fields = ['userID', 'autamaID']
        fields = ['matchID', 'userID', 'autamaID']

