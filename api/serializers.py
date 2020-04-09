from rest_framework import serializers
from .models import UserInfo, AutamaInfo, Matches, Messages


# NOTE: serializers turn models into json data to send thru service

# return user object as data
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo  # added image
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'gender',
                  'image', 'interest1', 'interest2', 'interest3', 'interest4', 'interest5', 'interest6']

    # (Overrides method in ModelSerializer)
    # Override create event to correctly encrypt password.
    def create(self, validated_data):
        user = UserInfo.objects.create_user(
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
        model = AutamaInfo   # added  autamaID & pickle
        fields = ['autamaID', 'creator', 'picture', 'first', 'last', 'num_matches', 'owner', 'pickle',
                  'interest1', 'interest2', 'interest3']
        # not returning interest4, interest5, interest6 for some personality intrigue/mystery
        # and do we need slug ret here?


# return Message object as data
class MessagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Messages   # added matchID, userID, autamaID
        fields = ['matchID', 'userID', 'autamaID', 'sender', 'timeStamp', 'messageTxt']
        # fields = ['sender', 'timeStamp', 'messageTxt']


# return list of User-Autama Matches
class MatchesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Matches
        fields = ['matchID', 'userID', 'autamaID']

