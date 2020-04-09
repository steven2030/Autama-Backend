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
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'gender',
                  'interest1', 'interest2', 'interest3', 'interest4', 'interest5']

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
        )
        return user


class AutamaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AutamaProfile
        fields = ['creator', 'picture', 'first', 'last', 'nummatches', 'owner',
                  'interest1', 'interest2', 'interest3']


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Messages
        fields = ['sender', 'timeStamp', 'message']
