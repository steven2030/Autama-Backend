from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse


class User(AbstractUser):
    gender = models.IntegerField(verbose_name="gender",
                                 choices=((0, 'Rather Not Say'), (1, 'Male'), (2, 'Female'),
                                          (3, 'Non-Conforming'), (4, 'Other')), default=0)
    image = models.ImageField(max_length=1000, upload_to='avatar', verbose_name=u'picture', null=True, blank=True)
    interest1 = models.TextField()
    interest2 = models.TextField()
    interest3 = models.TextField()
    interest4 = models.TextField()
    interest5 = models.TextField()

    def __str__(self):
        return '{id} {username} {first} {last}'.format(id=self.id, username=self.username,
                                                       first=self.first_name,last=self.last_name)


class Messages(models.Model):
    # Constants used for enum in sender
    USER = 'User'
    AUTAMA = 'Autama'
    SENDER_CHOICES = [
        (USER, 'User'),
        (AUTAMA, 'Autama'),
    ]

    message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)
    userID = models.ForeignKey('User', on_delete=models.CASCADE)
    autamaID = models.ForeignKey('AutamaProfile', on_delete=models.CASCADE)
    sender = models.CharField(max_length=6, choices=SENDER_CHOICES)

    def __str__(self):
        return '{userID} {autamaID}'.format(userID=self.userID, autamaID=self.autamaID)


class AutamaProfile(models.Model):
    autamaid = models.CharField(max_length=100, default="0")
    creator = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='Images', blank=True)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    nummatches = models.CharField(max_length=100, default='0000000', editable=False)
    # TODO: change owner to User.ForeignKey
    owner = models.CharField(max_length=100, default='FREE')
    pickle = models.CharField(max_length=100, default='PICKLE')
    interest1 = models.CharField(max_length=100)
    interest2 = models.CharField(max_length=100)
    interest3 = models.CharField(max_length=100)
    interest4 = models.CharField(max_length=100)
    interest5 = models.CharField(max_length=100)
    interest6 = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, null=True, blank=True, default='')

    def __str__(self):
        return '{pk} {first} {last}'.format(pk=self.pk, first=self.first, last=self.last)

    def get_slug(self):
        slug = '{} {}'.format(self.first, self.last)
        return slugify(slug)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk, 'slug': self.get_slug()})

