from rest_framework.test import APIRequestFactory


from django.test import TestCase
from django.db import models
from django.contrib.auth import get_user_model
from .models import UserInfo, AutamaInfo
# from .models import UserInfo, AutamaInfo, Matches, Messages
# from .models import *
# from django.contrib.auth.models import AbstractUser


# Create tests for models: AutamaInfo UserInfo Matches Messages
# Create tests for views
# Create tests for serialization


# Create your tests here.
factory = APIRequestFactory()
request = factory.post('/notes/', {'title': 'new idea'})


class AccountCreationTestCase(TestCase): # class TestApi(TestCase):

    # set up models
    def setUpTestData(self):

        # Create 2 superusers for testing

        UserInfo.objects.create_superuser(
            username='smiley',
            password='Autama4life!',
            first_name='smiley',
            last_name='smiley',
            email='smiley@smile.com',
            gender='0',
            image='',
            interest1='1',
            interest2='2',
            interest3='3',
            interest4='4',
            interest5='5',
            interest6='6'
        )

        UserInfo.objects.create_superuser(
            username='smileyy',
            password='Autama4life!',
            first_name='smileyy',
            last_name='smileyy',
            email='smileyy@smile.com',
            gender='2',
            image='',
            interest1='11',
            interest2='22',
            interest3='33',
            interest4='44',
            interest5='55',
            interest6='66'
        )

        # Create 10 regular users for testing

        UserInfo.objects.create_user(
            username='testbob1',
            password='Autama4Life!',
            first_name='bob1',
            last_name='cob',
            email='bob1@cob.com',
            gender='0',
            image='',
            interest1='bob-ski',
            interest2='bob-cat',
            interest3='bob-ble',
            interest4='bob-by',
            interest5='bob-bin',
            interest6='bob-bye'
        )

        UserInfo.objects.create_user(
            username='testbob2',
            password='Autama4Life!',
            first_name='bob2',
            last_name='cob',
            email='bob2@cob.com',
            gender='1',
            image='',
            interest1='bob-ski',
            interest2='bob-cat',
            interest3='bob-ble',
            interest4='bob-by',
            interest5='bob-bin',
            interest6='bob-bye'
        )

        UserInfo.objects.create_user(
            username='testbob3',
            password='Autama4Life!',
            first_name='bob3',
            last_name='cob',
            email='bob3@cob.com',
            gender='2',
            image='',
            interest1='bob-ski',
            interest2='bob-cat',
            interest3='bob-ble',
            interest4='bob-by',
            interest5='bob-bin',
            interest6='bob-bye'
        )

        UserInfo.objects.create_user(
            username='testbob4',
            password='Autama4Life!',
            first_name='bob4',
            last_name='cob',
            email='bob4@cob.com',
            gender='3',
            image='',
            interest1='bob-ski',
            interest2='bob-cat',
            interest3='bob-ble',
            interest4='bob-by',
            interest5='bob-bin',
            interest6='bob-bye'
        )

        UserInfo.objects.create_user(
            username='testbob5',
            password='Autama4Life!',
            first_name='bob5',
            last_name='cob',
            email='bob5@cob.com',
            gender='4',
            image='',
            interest1='bob-ski',
            interest2='bob-cat',
            interest3='bob-ble',
            interest4='bob-by',
            interest5='bob-bin',
            interest6='bob-bye'
        )

        UserInfo.objects.create_user(
            username='testanne6',
            password='Autama4Life!',
            first_name='anne6',
            last_name='span',
            email='anne6@span.com',
            gender='0',
            image='',
            interest1='anne-droid',
            interest2='anne-teek',
            interest3='anne-chovies',
            interest4='anne-honor',
            interest5='anne-dooie',
            interest6='anne-thropology'
        )

        UserInfo.objects.create_user(
            username='testanne7',
            password='Autama4Life!',
            first_name='anne7',
            last_name='span',
            email='anne7@span.com',
            gender='1',
            image='',
            interest1='anne-droid',
            interest2='anne-teek',
            interest3='anne-chovies',
            interest4='anne-honor',
            interest5='anne-dooie',
            interest6='anne-thropology'
        )

        UserInfo.objects.create_user(
            username='testanne8',
            password='Autama4Life!',
            first_name='anne8',
            last_name='span',
            email='anne8@span.com',
            gender='2',
            image='',
            interest1='anne-droid',
            interest2='anne-teek',
            interest3='anne-chovies',
            interest4='anne-honor',
            interest5='anne-dooie',
            interest6='anne-thropology'
        )

        UserInfo.objects.create_user(
            username='testanne9',
            password='Autama4Life!',
            first_name='anne9',
            last_name='span',
            email='anne9@span.com',
            gender='3',
            image='',
            interest1='anne-droid',
            interest2='anne-teek',
            interest3='anne-chovies',
            interest4='anne-honor',
            interest5='anne-dooie',
            interest6='anne-thropology'
        )

        UserInfo.objects.create_user(
            username='testanne10',
            password='Autama4Life!',
            first_name='anne10',
            last_name='span',
            email='anne10@span.com',
            gender='4',
            image=models.ImageField('user_pics/a0'),  # just a test
            interest1='anne-droid',
            interest2='anne-teek',
            interest3='anne-chovies',
            interest4='anne-honor',
            interest5='anne-dooie',
            interest6='anne-thropology'
        )


        # Now create 10 Autama Profiles

        AutamaInfo.objects.create(
            autamaID='01testHAL',
            creator='The Autama Team OGs',
            picture=models.ImageField(upload_to='autama_pics', blank=True),  # testing what is added here
            first='01HAL',
            last='LEE',
            num_matches=0000000,
            owner=models.ForeignKey(get_user_model(), on_delete=models.PROTECT, default="UNCLAIMED"),  # owner can change
            pickle='01testHAL-PICKLE',
            interest1='HAL-LO',
            interest2='HAL-ITOSIS',
            interest3='HAL-BERD',
            interest4='HAL-LELUJAH',
            interest5='HAL-DO',
            interest6='HAL-LEE',
        )

        AutamaInfo.objects.create(
            autamaID='02testHAL',
            creator='The Autama Team OGs',
            picture=models.ImageField(name='autama_pics/a02'),  # another test
            first='02HAL',
            last='LEE',
            num_matches=0000000,
            owner=models.ForeignKey(get_user_model(), on_delete=models.PROTECT, default="UNCLAIMED"),
            pickle='02testHAL-PICKLE',
            interest1='HAL-LO',
            interest2='HAL-ITOSIS',
            interest3='HAL-BERD',
            interest4='HAL-LELUJAH',
            interest5='HAL-DO',
            interest6='HAL-LEE',
        )

        AutamaInfo.objects.create(
            autamaID='03testHAL',
            creator='The Autama Team OGs',
            picture='autama_pics/a03',         # another test
            first='03HAL',
            last='LEE',
            num_matches=0000000,
            owner=models.ForeignKey(get_user_model(), on_delete=models.PROTECT, default="UNCLAIMED"),
            pickle='03testHAL-PICKLE',
            interest1='HAL-LO',
            interest2='HAL-ITOSIS',
            interest3='HAL-BERD',
            interest4='HAL-LELUJAH',
            interest5='HAL-DO',
            interest6='HAL-LEE',
        )

        AutamaInfo.objects.create(
            autamaID='04testHAL',
            creator='The Autama Team OGs',
            picture='',
            first='04HAL',
            last='LEE',
            num_matches=0000000,
            owner=models.ForeignKey(get_user_model(), on_delete=models.PROTECT, default="UNCLAIMED"),
            pickle='04testHAL-PICKLE',
            interest1='HAL-LO',
            interest2='HAL-ITOSIS',
            interest3='HAL-BERD',
            interest4='HAL-LELUJAH',
            interest5='HAL-DO',
            interest6='HAL-LEE',
        )

        AutamaInfo.objects.create(
            autamaID='05testHAL',
            creator='The Autama Team OGs',
            picture='',
            first='05HAL',
            last='LEE',
            num_matches=0000000,
            owner=models.ForeignKey(get_user_model(), on_delete=models.PROTECT, default="UNCLAIMED"),
            pickle='05testHAL-PICKLE',
            interest1='HAL-LO',
            interest2='HAL-ITOSIS',
            interest3='HAL-BERD',
            interest4='HAL-LELUJAH',
            interest5='HAL-DO',
            interest6='HAL-LEE',
        )

        AutamaInfo.objects.create(
            autamaID='06testHAL',
            creator='The Autama Team OGs',
            picture='',
            first='06HAL',
            last='LEE',
            num_matches=0000000,
            owner=models.ForeignKey(get_user_model(), on_delete=models.PROTECT, default="UNCLAIMED"),
            pickle='06testHAL-PICKLE',
            interest1='HAL-LO',
            interest2='HAL-ITOSIS',
            interest3='HAL-BERD',
            interest4='HAL-LELUJAH',
            interest5='HAL-DO',
            interest6='HAL-LEE',
        )

        AutamaInfo.objects.create(
            autamaID='07testHAL',
            creator='The Autama Team OGs',
            picture='',
            first='07HAL',
            last='LEE',
            num_matches=0000000,
            owner=models.ForeignKey(get_user_model(), on_delete=models.PROTECT, default="UNCLAIMED"),
            pickle='07testHAL-PICKLE',
            interest1='HAL-LO',
            interest2='HAL-ITOSIS',
            interest3='HAL-BERD',
            interest4='HAL-LELUJAH',
            interest5='HAL-DO',
            interest6='HAL-LEE',
        )

        AutamaInfo.objects.create(
            autamaID='08testHAL',
            creator='The Autama Team OGs',
            picture='',
            first='08HAL',
            last='LEE',
            num_matches=0000000,
            owner=models.ForeignKey(get_user_model(), on_delete=models.PROTECT, default="UNCLAIMED"),
            pickle='08testHAL-PICKLE',
            interest1='HAL-LO',
            interest2='HAL-ITOSIS',
            interest3='HAL-BERD',
            interest4='HAL-LELUJAH',
            interest5='HAL-DO',
            interest6='HAL-LEE',
        )

        AutamaInfo.objects.create(
            autamaID='09testHAL',
            creator='The Autama Team OGs',
            picture='',
            first='09HAL',
            last='LEE',
            num_matches=0000000,
            owner=models.ForeignKey(get_user_model(), on_delete=models.PROTECT, default="UNCLAIMED"),
            pickle='09testHAL-PICKLE',
            interest1='HAL-LO',
            interest2='HAL-ITOSIS',
            interest3='HAL-BERD',
            interest4='HAL-LELUJAH',
            interest5='HAL-DO',
            interest6='HAL-LEE',
        )

        AutamaInfo.objects.create(
            autamaID='10testHAL',
            creator='The Autama Team OGs',
            picture='',
            first='10HAL',
            last='LEE',
            num_matches=0000000,
            owner=models.ForeignKey(get_user_model(), on_delete=models.PROTECT, default="UNCLAIMED"),
            pickle='10testHAL-PICKLE',
            interest1='HAL-LO',
            interest2='HAL-ITOSIS',
            interest3='HAL-BERD',
            interest4='HAL-LELUJAH',
            interest5='HAL-DO',
            interest6='HAL-LEE',
        )


# Stuff to  delete later

# UserInfo: ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'gender',
#            'image', 'interest1', 'interest2', 'interest3', 'interest4', 'interest5', 'interest6']
# AutamaInfo:['autamaID', 'creator', 'picture', 'first', 'last', 'num_matches', 'owner', 'pickle',
#                   'interest1', 'interest2', 'interest3']
# Matches:
# Messages:

# questions about picture load/uploads
# owner = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, default="")
# image = models.ImageField(max_length=1000, upload_to='avatar', verbose_name=u'picture', null=True, blank=True)
# picture = models.ImageField(upload_to='Images', blank=True)


# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from api.apps.core.models import Account
#
# class AccountTests(APITestCase):
#     def test_create_account(self):
#         """
#         Ensure we can create a new account object.
#         """
#         url = reverse('account-list')
#         data = {'name': 'DabApps'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Account.objects.count(), 1)
#         self.assertEqual(Account.objects.get().name, 'DabApps')
