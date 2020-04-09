from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse


# user model info
# TODO: Would it be useful to add num_matches trait? (email&password created @ api/serializers.py)
class UserInfo(AbstractUser):
    gender = models.IntegerField(verbose_name="gender",
                                 choices=((0, 'Rather Not Say'), (1, 'Male'), (2, 'Female'),
                                          (3, 'Non-Conforming'), (4, 'Other')), default=0)
    image = models.ImageField(max_length=1000, upload_to='user_pics', null=True, blank=True)  # removed verbose_name=u'picture'
    interest1 = models.TextField()
    interest2 = models.TextField()
    interest3 = models.TextField()
    interest4 = models.TextField()
    interest5 = models.TextField()
    interest6 = models.TextField()

    # Overrides method in AbstractBaseUser
    def __str__(self):
        return '{id} {username} {first} {last}'.format(id=self.id, username=self.username,
                                                       first=self.first_name, last=self.last_name)


# autama model info
class AutamaInfo(models.Model):
    autamaID = models.CharField(max_length=100, default="0")
    creator = models.CharField(max_length=100, default='Team Autama OGs')
    picture = models.ImageField(max_length=1000, upload_to='autama_pics', blank=True)  # this is uploading a pic
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    num_matches = models.CharField(max_length=100, default='0000000', editable=False)
    owner = models.ForeignKey(get_user_model(),  on_delete=models.PROTECT, default="UNCLAIMED")  # owner can change
    pickle = models.CharField(max_length=100, default='PICKLE')  # do we still need this?
    interest1 = models.CharField(max_length=100)
    interest2 = models.CharField(max_length=100)
    interest3 = models.CharField(max_length=100)
    interest4 = models.CharField(max_length=100)
    interest5 = models.CharField(max_length=100)
    interest6 = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, null=True, blank=True, default='')

    # overrides method in Model
    # def __str__(self):
    #     return '{pk} {first} {last}'.format(pk=self.pk, first=self.first, last=self.last)

    def get_slug(self):
        slug = '{} {}'.format(self.first, self.last)
        return slugify(slug)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk, 'slug': self.get_slug()})


# user-autama matches model
class Matches(models.Model):
    matchID = models.IntegerField(primary_key=True, default=None)   # pk
    userID = models.ForeignKey('UserInfo', on_delete=models.CASCADE,)
    autamaID = models.ForeignKey('AutamaInfo', on_delete=models.CASCADE,)

    # TODO: Make sure when a match is created(matchID != None) increment autama num_matches somewhere
    # overrides method in model
    # def __str__(self):
    #     return '{userID} {autamaID}'.format(userID=self.userID, autamaID=self.autamaID)


# messages for specific conversations bot-to-user
class Messages(models.Model):
    # Constants used for enum in sender
    USER = 'User'
    AUTAMA = 'Autama'
    SENDER_CHOICES = [
        (USER, 'User'),
        (AUTAMA, 'Autama'),
    ]
    # TODO: Add a way to pull matchID in from Matches
    matchID = models.ForeignKey('Matches', on_delete=models.CASCADE, default=None)
    userID = models.ForeignKey('UserInfo', on_delete=models.CASCADE)  # del later?
    autamaID = models.ForeignKey('AutamaInfo', on_delete=models.CASCADE)  # del later?
    timeStamp = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=6, choices=SENDER_CHOICES)
    messageTxt = models.TextField()

    # overrides method in model
    # def __str__(self):
    #     return '{sender} {timeStamp} {messageTxt}'.format(sender=self.sender,
    #                                                       timeStamp=self.timeStamp, messageTxt=self.messageTxt)

