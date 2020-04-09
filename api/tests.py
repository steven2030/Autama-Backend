from django.test import TestCase
# from .models import *
from .models import UserInfo, AutamaInfo, Matches, Messages

from django.contrib.auth.models import AbstractUser

# Create test for views
# Create test for models -AutamaInfo UserInfo Matches Messages
# Create test for serialization?

# UserInfo: ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'gender',
#            'image', 'interest1', 'interest2', 'interest3', 'interest4', 'interest5', 'interest6']

# Create your tests here.
class TestApi(TestCase):
    # set up models
    def setUpTestData(self):

        UserInfo.objects.create_user(
            username='testbob1',
            password='',
            first_name='',
            last_name='',
            email='',
            gender='',
            image='',
            interest1='',
            interest2='',
            interest3='',
            interest4='',
            interest5='',
            interest6=''
        )

        UserInfo.objects.create_user(
            username='testbob1',
            password='',
            first_name='',
            last_name='',
            email='',
            gender='',
            image='',
            interest1='',
            interest2='',
            interest3='',
            interest4='',
            interest5='',
            interest6=''
        )

        UserInfo.objects.create_user(
            username='testbob1',
            password='',
            first_name='',
            last_name='',
            email='',
            gender='',
            image='',
            interest1='',
            interest2='',
            interest3='',
            interest4='',
            interest5='',
            interest6=''
        )

        UserInfo.objects.create_user(
            username='testbob1',
            password='',
            first_name='',
            last_name='',
            email='',
            gender='',
            image='',
            interest1='',
            interest2='',
            interest3='',
            interest4='',
            interest5='',
            interest6=''
        )

        UserInfo.objects.create_user(
            username='testbob1',
            password='',
            first_name='',
            last_name='',
            email='',
            gender='',
            image='',
            interest1='',
            interest2='',
            interest3='',
            interest4='',
            interest5='',
            interest6=''
        )

        UserInfo.objects.create_user(
            username='testbob1',
            password='',
            first_name='',
            last_name='',
            email='',
            gender='',
            image='',
            interest1='',
            interest2='',
            interest3='',
            interest4='',
            interest5='',
            interest6=''
        )

